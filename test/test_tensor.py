import numpy as np
import pytest
import mechkit
from mechkit.operators import Sym_Fourth_Order_Special
from homopy.tensor import *


@pytest.fixture()
def random_hooke_sym():
    return mechkit.operators.Sym_Fourth_Order_Special(label="inner")(
        np.random.rand(3, 3, 3, 3)
    )


@pytest.fixture()
def random_complete_sym():
    return mechkit.operators.Sym_Fourth_Order_Special(label="complete")(
        np.random.rand(3, 3, 3, 3)
    )


@pytest.fixture(name="mechkit_converter")
def set_up_implicit_mechkit_converter():
    return mechkit.notation.Converter()


def test_orthogonal_base():
    t = Tensor()

    orthogonal_base = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    tensor_base = np.vstack((t.e1, t.e2, t.e3))

    assert np.allclose(orthogonal_base, tensor_base, rtol=1e-6)


class Test_Converter:
    def test_random_mandel_to_tensor_and_back(self):
        t = Tensor()
    
        random_mat = np.random.rand(6, 6)
        random_mat_sym = 1 / 2 * (random_mat + random_mat.T)
    
        random_tensor_sym = t.mandel2tensor(random_mat_sym)
        recovered_mat = t.tensor2mandel(random_tensor_sym)
    
        assert np.allclose(random_mat_sym, recovered_mat, rtol=1e-6)

    @pytest.mark.parametrize(
        "fixture_name", ["random_hooke_sym", "random_complete_sym"]
    )
    def test_compare_with_mechkit(self, fixture_name, mechkit_converter, request):

        # Get the random tensors which are stored as fixture following
        # https://engineeringfordatascience.com/posts/pytest_fixtures_with_parameterize/
        random_tensor = request.getfixturevalue(fixture_name)

        mandel_homopy = Tensor().tensor2mandel(random_tensor)
        mandel_mechkit = mechkit_converter.to_mandel6(random_tensor)

        assert np.allclose(mandel_homopy, mandel_mechkit)




