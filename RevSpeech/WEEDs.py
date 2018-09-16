import json

listy = []
evenmorelist =[]

with open('data.json') as f:
    data = json.load(f)

for i in range(0,(len(data['monologues'][0]['elements']))):
    try:
        first_start_time = round((data["monologues"][0]['elements'][i]['ts']),3)
        first_end_time = round((data["monologues"][0]['elements'][i]['end_ts']),3)
        # Do something.

        listy.append(first_start_time)
        listy.append(first_end_time)

        pass

    except:

        continue

print (listy)

for i in range(0,len(listy),4):
    try:
        if (listy[i + 2]-listy[i + 1])>0.45:
            evenmorelist.append((listy[i + 1],listy[i + 2]))
        pass

    except:

        continue

print (evenmorelist)

with open("moredata", "w") as output:
    output.write(str(evenmorelist))





