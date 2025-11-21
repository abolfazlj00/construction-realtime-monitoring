from abc import ABC, abstractmethod
from datetime import date
from typing import NamedTuple


class IdentityInfo(NamedTuple):
    """
    Result of identity validation containing person's information.
    """
    first_name: str
    last_name: str
    is_valid: bool


class IdentityValidatorInterface(ABC):
    """
    Abstract interface for identity validation service.
    This should be implemented with actual API integration (e.g., Saman, Zarinpal, etc.)
    """

    @abstractmethod
    async def validate_identity(
        self,
        national_code: str,
        birthday: date,
        mobile: str
    ) -> IdentityInfo:
        """
        Validates that:
        1. National code and birthday are correct
        2. Mobile number belongs to the person with this national code
        3. Returns the person's name if validation succeeds

        Args:
            national_code: 10-digit Iranian national code
            birthday: Person's birthday (Gregorian date)
            mobile: Normalized mobile number (e.g., "9191234567")

        Returns:
            IdentityInfo with first_name, last_name, and is_valid=True if all checks pass

        Raises:
            ValueError: If validation fails (invalid national code, wrong birthday, 
                       mobile doesn't match, etc.)
        """
        pass


class IdentityValidator(IdentityValidatorInterface):
    """
    Default implementation of identity validator.
    TODO: Replace with actual API integration (Saman, Zarinpal, government API, etc.)
    """

    async def validate_identity(
        self,
        national_code: str,
        birthday: date,
        mobile: str
    ) -> IdentityInfo:
        """
        Placeholder implementation - replace with actual API call.
        
        Example implementation structure:
        - Call external API with national_code, birthday, mobile
        - API should verify:
          1. National code is valid
          2. Birthday matches the national code
          3. Mobile number is registered to this person
        - Return person's name if all validations pass
        """
        
        # TODO: Implement actual API integration
        # Example:
        # response = await self._call_identity_api(national_code, birthday, mobile)
        # if not response.is_valid:
        #     raise ValueError("Identity validation failed: ...")
        # return IdentityInfo(
        #     first_name=response.first_name,
        #     last_name=response.last_name,
        #     is_valid=True
        # )
        
        # Placeholder - remove this and implement actual validation
        raise NotImplementedError(
            "Identity validation not implemented. "
            "Please implement IdentityValidator.validate_identity() with actual API integration."
        )

