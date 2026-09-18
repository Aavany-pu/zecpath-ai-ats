def check_access(user_role, required_role):
    if user_role == required_role:
        return {
            "Status": "Access Granted",
            "Access Allowed": True
        }

    return {
        "Status": "Access Denied",
        "Access Allowed": False
    }


def evaluate_access_request(user_role, required_role, resource):
    access_result = check_access(
        user_role,
        required_role
    )

    return {
        "Status": "Access Control Evaluated",
        "User Role": user_role,
        "Required Role": required_role,
        "Resource": resource,
        "Access Result": access_result
    }