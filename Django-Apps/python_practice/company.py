d = {
      "employee" : [{"firstname":"John","lastname":"Doe"},
                    {"firstname":"Anna","lastname":"Smith"},
                    {"firstname":"peter","lastname":"Jones"}
                    ],
      "owners" : [{"firstname":"Jack","lastname":"Petter"},
                  {"firstname":"Jessy","lastname":"Petter"}

                  ]
}
import json
with open("company.json","w") as file :
    json.dump(d,file,indent=2)

