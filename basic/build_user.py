def build_profile(first_name, last_name, **other_infos):
    user = {}
    user['first_name'] = first_name
    user['last_name'] = last_name

    if other_infos:
        for key, value in other_infos.items():
            user[key] = value
    
    return user