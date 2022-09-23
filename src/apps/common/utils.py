from rest_framework import status

CREATED_BODY = dict(
    message="successfully created",
    status_code=status.HTTP_201_CREATED,
)

SUCCESS_BODY = dict(
    message="login successfully",
    status_code=status.HTTP_200_OK,
)

FAILURE_BODY = dict(
    message="login failed",
    status_code=status.HTTP_400_BAD_REQUEST,
)

UPDATE_BODY = dict(
    message="successfully updated",
    status_code=status.HTTP_200_OK,
)

INVALID_CONTENT = dict(
    message="Bad content was provided",
    status_code=status.HTTP_400_BAD_REQUEST,
)

GENERAL_SUCCESS_BODY = dict(
    message="successful",
    status_code=status.HTTP_200_OK,
)
