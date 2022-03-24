import pytest
from pydantic import ValidationError


def build_test_model_class(model):
    """Create a test class for pydantic model validation.

    Create and return a test class that validates if a given model correctly:

    * build and validate itself if data is valid.
    * build but raises ValidationError if data is invalid.
    * is immutable.
    * has correct JSON encoders.

    The caller MUST implement two fixtures into the parent test class for correct
    behaviour:

    * valid_data: a fixture that returns a dict with valid keys and values.
    * invalid_data: a fixture that returns a dict with valid keys but invalid values.

    :param model: Pydantic model which is subject to test.
    :returns: a custom TestModel class which implements test functions calling model
    as subject.
    """

    class TestModel:
        """Test entire model validation."""

        def test_validation(self, valid_data):
            assert model(**valid_data)

        def test_invalidation(self, invalid_data):
            with pytest.raises(ValidationError):
                model(**invalid_data)

        def test_immutability(self, valid_data):
            entity = model(**valid_data)
            for key in entity.dict().keys():
                with pytest.raises(TypeError):
                    setattr(entity, key, "some value")

        def test_json_encoders(self, valid_data):
            entity = model(**valid_data)
            assert entity.json()

    return TestModel
