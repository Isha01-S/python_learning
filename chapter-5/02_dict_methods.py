marks={
        "isha":100,
        "shubham":55,
        "Rahul":23,
        0: "isha"
    }
print(marks.items())
print(marks.keys())
print(marks.values())

marks.update({"isha":99,"renuka":100})

print(marks)

print(marks.get("shivika"))#prints none
print(marks.get("isha"))
print(marks["shivika"])#returns an error