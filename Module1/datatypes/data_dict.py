school_names = {
    "id": 1,
    "registered_type": "Govt. School",
    "names": ["Don Bosco", "MKV", "Chettinad public", "JothiVimal"],
    "city": "Coimbatore",
    "tollfree": 1800415654
} # key-value pair key : value

print(school_names)
print(type(school_names))
print("\n")
city = school_names["city"]
print(type(city))
print(city)
print(school_names["names"][0])
print(school_names["names"][-4])
print(school_names["names"][-1])