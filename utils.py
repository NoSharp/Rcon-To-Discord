def is_author(author) -> bool:
    for role in author.roles:
        if role.name == "Admin":
            return True

    return False
