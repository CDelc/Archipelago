
# {roomName}*{checkpointName} = checkpoint
# {roomName}${strawberry entity ID} = strawberry room
# &{roomName} = branch room (can only do depth of 1 automatically)
# >{roomName} = 1 way transition from previous
# #{roomName} = excluded from room checks
# ,@, = Main route ended, extra rooms listed after this point

# order of operations: &>#{roomName}*{checkpointName}${strawberry ID}${strawberry ID 2}...

one_b : str = "00, >01, >02, >02b, >03, 04*Crossing, >05, >05b, >06, 07, >08*Chasm, >08b, >09, 10, >11, >end"
one_c : str = "00, >01, >02"

seven_a : str = (
    "a-00, a-01, a-02, &a-02b$61, a-03, a-04, &a-04b$136$85, a-05$54, a-06,"
    ">b-00*500m, >b-01, b-02, &b-02b$102, b-03, &b-04$67, >b-05, b-06, b-07, b-08$129, b-09$167,"
    ">c-00*1000m, >c-01, >c-02, >c-03, &c-03b$228, >c-04, &c-05$248, &c-06, c-06b$218, &c-06c, >c-07, &c-07b$291, c-08$331, c-09$354,"
    ">d-00*1500m$43, d-01, d-01b, &d-01c$226, d-02, d-03$383, &d-03b, d-04$388, d-05, &d-05b, d-06, &d-07$484, &d-08$527, d-09, >d-10, &d-10b$682, d-11,"
    ">e-00b*2000m, >e-00, &e-02$7, e-03, >e-04, e-05$237, e-06, e-07, e-08, &e-09$398, e-10$515, e-10b, >e-13$829,"
    ">f-00*2500m$590, &f-01$639, f-02, &f-02, f-04, >f-03, >f-05, &f-07$711, &f-06, f-08, &f-08b$856, >f-09, >f-10, >f-10b, >f-11$1068$1229$1238,"
    ">g-00*3000m, >g-00b$37$127$114, >g-01$66$279$342, >g-02, >g-03$1504,"
    "@, b-02e$112, b-02c, &b-02d, d-01d$282, e-01, &e-01b, e-01c, e-11$425, &e-12$504, f-08d, &>f-08c$759"
)


levelSummary: str = seven_a


def extractRoomName(name: str):
    return name.replace(" ", "").split("*")[0].split("$")[0].replace("&", "").replace(">", "").replace("#", "")



rooms: list[str] = levelSummary.split(",")

prev_room = ""

end_reached = False

index = 0

python_room_output = []
csharp_output = []

while index < len(rooms):
    room_name = rooms[index].replace(" ", "")
    if not room_name == "@":
        room_args = []

        branch = room_name.startswith("&")
        one_way = room_name.replace("&", "").startswith(">")
        exclude = room_name.replace("&", "").replace(">", "").startswith("#")
        checkpoint = room_name.split("*")[1].split("$")[0] if "*" in room_name else ""
        strawberry_entity_ids = room_name.split("$")[1:]
        
        branch_rooms = []
        if not branch and end_reached:
            prev_room = ""
        
        j = index + 1
        while j < len(rooms) and rooms[j].replace(" ", "").startswith("&"):
            branch_rooms.append(rooms[j])
            j = j + 1
            
        next_room_index = j
        next_room = ""
        
        if next_room_index < len(rooms):
            next_room = rooms[next_room_index]
            
        if next_room == "@":
            end_reached = True
            
        if branch:
            next_room = ""
            branch_rooms = []
            
        transitions: list[str] = []
        locations: list[str] = []
        
        if next_room and not end_reached and not branch:
            transitions.append(f"Transition(\"{extractRoomName(next_room)}\")")
        if prev_room and not one_way:
            transitions.append(f"Transition(\"{extractRoomName(prev_room)}\")")
            
        for branch_room in branch_rooms:
            transitions.append(f"Transition(\"{extractRoomName(branch_room)}\")")
            
        for strawberry in strawberry_entity_ids:
            locations.append(f"Location(LocationType.STRAWBERRY, {strawberry})")
        
        if not branch:
            prev_room = room_name
            
        room_args.append(str(index))
        room_args.append(f"[{", ".join(transitions)}]")
        if len(locations) > 0:
            room_args.append(f"[{", ".join(locations)}]")
        if index == 0:
            room_args.append("start_room=True")
        if checkpoint:
            room_args.append(f"checkpoint=\"{checkpoint}\"")
        if exclude:
            room_args.append("excluded=True")
        python_room_output.append(f"\"{extractRoomName(room_name)}\": Room({", ".join(room_args)})")
        csharp_output.append(f"{{{index}, \"{extractRoomName(room_name)}\"}}")
    else:
        end_reached = True
        prev_room = ""
        
    index = index + 1
    
print(f"\t{",\n\t".join(python_room_output)}")
print("\n\n")
print("new Dictionary<long, string>\n{")
print(f"\t{",\n\t".join(csharp_output)}")
print("}")