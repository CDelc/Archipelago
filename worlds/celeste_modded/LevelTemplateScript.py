
# {roomName}*{checkpointName} = checkpoint
# {roomName}${strawberry entity ID} = strawberry room
# &{roomName} = branch room (can only do depth of 1 automatically)
# >{roomName} = 1 way transition from previous
# #{roomName} = excluded from room checks
# ,@, = Main route ended, extra rooms listed after this point

# order of operations: &>#{roomName}*{checkpointName}${strawberry ID}${strawberry ID 2}...

one_b : str = "00, >01, >02, >02b, >03, 04*Crossing, >05, >05b, >06, 07, >08*Chasm, >08b, >09, 10, >11, >end"
one_c : str = "00, >01, >02"
two_a : str = ("start, &s0, 0, &1$1, 3x,"
               "3*CheckpointOne, >4$4, >5$15, >6, >7, >8$18, >9$22, &9b$5, >10$27, >2, 11, 12b, &12c$7, &12d$44, 12, 13,"
               ">end_0*CheckpointTwo, end_1, end_2, end_3, end_4, end_3b, end_5, end_6,"
               "@, s1, &s2, d0$6, &d1$67, &d6$2, &d9, &d7, &d2$9$31, &d4$6, d5$12, d8, &>d3, end_s0, &end_s1, end_3cb, &end_3c$13")
two_b : str = "start, 00, >01, >01b, >02b, >02, >03*CheckpointOne, >04, >05, >06, >07, >08b*CheckpointTwo, >08, >10, >11, >end"
two_c : str = "00, >01, >02"
three_a: str = ("s0, s1, s2$6$18, s3$2, 0x-a, 00a$5, >02-a, &02-b, 03-a, &04-b$14, 05-a, 06-a$7, >07-a, >08-a*CheckpointOne,"
                "&08-x$4, 09-b, >09-d*CheckpointTwo, >08-d, >06-d$238, >04-d, 04-c$40, >02-d,"
                "00-d*CheckpointThree, >roof00, >roof01, >roof02, >roof03$97, >roof04, >roof05, >roof06b, >roof06$276$308, >roof07,"
                "@, 01-b, 00-b$42, 00-c, 0x-b, 07-b$4, 06-b$14, 06-c$3, 05-c$2, 08-c, 08-b, 10-x, 11-x, 11-y, 12-y$1, 11-z, 10-z, 10-y$2, 11-b, 12-b, 13-b$31, 13-a, 13-x$13, 12-x, 11-a, 10-c, 11-c, 12-c$1, 12-d, 11-d$52, 10-d, 03-b, 01-c, 03-b$1$25")
three_b: str = "00, &back, >01, >02, >03, >04, >05, >06, >07, >08, >09, >10, >11, >13, >14, >15, >12, >16, >17, >18, >19, >21, >20, >end"
four_a: str = ("a-00, >a-01, >a-01x$11, >a-02, >a-03$33, >a-04, >a-05, >a-06$6, >a-07$16, >a-08, &a-10$13, >a-09$12,"
               ">b-00*CheckpointOne, &b-01$13$6, &b-03$5, &b-04$1, >b-02, &b-sec, >b-05, >b-08b, >b-08$11,"
               ">c-00*CheckpointTwo$17, &c-01$26, >c-02, >c-04, >c-05$21, >c-06$35, &c-06b$43, >c-09, >c-07, >c-08$28, &c-10$55,"
               ">d-00*CheckpointThree, &d-00b$11, >d-01$7, >d-02, >d-03, >d-04$88, >d-05, >d-06, >d-07$70, >d-08, >d-09$18, d-10,"
               "@,a-11, b-06, &>b-07$15, b-secb")
four_b: str = "a-00, >a-01, >a-02, >a-03, >a-04, >b-00*CheckpointOne, >b-01, >b-02, >b-03, >b-04, >c-00*CheckpointTwo, >c-01, >c-02, >c-03, >c-04, >d-00*CheckpointThree, >d-01, >d-02, >d-03, >end"

five_a: str = ("a-00x$7, >a-00b, >a-00d, >a-00c, >a-00, >a-01$256, &a-04$2, &a-02$23, &a-08, a-13,"
               ">b-00*CheckpointOne, &b-18$2, >b-01, &b-20$189$183, &b-01c$85, >b-01b, >b-02, &b-03$24, &b-05$23, &b-04, &b-10$4, &b-11, >b-06, >b-19, >b-14, &b-15, >b-16,"
               ">c-00*CheckpointTwo, >c-01, >c-01b, >c-01c, >c-08b, >c-08$112, >c-10, >c-12, >c-07, >c-11, >c-09, >c-13,"
               ">c-13*CheckpointThree, >d-01, &d-09, >d-04$35$126, >d-19$533, >d-19b, >d-10, >d-20,"
               ">e-00*CheckpointFour, >e-01, >e-02, >e-03, >e-04, >e-06$56, >e-05, >e-07, >e-08, >e-09, >e-10, >e-11,"
               "@,a-03$4, a-05$22, &a-06$2, &a-07$6, a-14$12, a-09, &a-10, &a-11$2, a-12, a-15, b-21$99, b-08, &b-07, &>b-09, b-12$42, b-17$14, &b-13, &b-22, d-15$336$217, &d-13$199, d-05, &>d-06, d-02, &>d-03, d-07")
five_b: str = "start, >a-00, >a-01, >a-02, >b-00*CheckpointOne, &b-06, &b-01, >b-02, &b-05, >b-08, >b-09, >c-00*CheckpointTwo, >c-01, >c-02, >c-03, >c-04, >d-00*CheckpointThree, >d-01, >d-02, >d-03, >d-04, >d-05, @, b-07, &>b-03, b-04"
six_a: str = ("start, >00*CheckpointOne, >01, >02, >03, >02b, >04, &04e, &04b, >05, >06, >07, &>08b, >08a, >09, &>10b, >10a, >11, &>12b, >12a, >13, &>14b, >14a, >15, &>16b, >16a, >17, &>18b, >18a, >19, >20,"
              "b-00*CheckpointTwo, >b-01, >b-02, >b-02b, >b-03,"
              "boss-00*CheckpointThree, >boss-01, >boss-02, >boss-03, >boss-04, >boss-05, >boss-06, >boss-07, >boss-08, >boss-09, >boss-10, >boss-11, >boss-12, >boss-13, >boss-14, >boss-15, >boss-16, >boss-17, >boss-18, >boss-19, >boss-20,"
              "after-00*CheckpointFour, after-01, after-02,"
              "@, 04c, #b-00b, &#b-00c")

six_b: str = "a-00, >a-01, >a-02, >a-03, >a-04, >a-05, >a-06, >b-00*CheckpointOne, >b-01, >b-02, >b-03, >b-04, >b-05, >b-06, >b-07, >b-08, >b-09, >b-10, >c-00*CheckpointTwo, >c-01, >c-02, >c-03, >c-04, >d-00*CheckpointThree, >d-01, >d-02, >d-03, >d-04, >d-05"

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
seven_b: str = "a-00, >a-01, >a-02, >a-03, >b-00*500m, >b-01, >b-02, >b-03, >c-01*1000m, >c-00, >c-02, >c-03, >d-00*1500m, >d-01, >d-02, >d-03, >e-00*2000m, >e-01, >e-02, >e-03, >f-00*2500m, >f-01, >f-02, >f-03, >g-00*3000m, >g-01, >g-02, >g-03"

eight_a: str = ("00, &0x, 01, 02, >a-00*CheckpointOne, >a-01, >a-02, >a-03, >b-00, &b-06$174, >b-07b, >b-07,"
                ">c-00*CheckpointTwo, &c-00b$211, c-01, >c-02$248, >c-03, &c-03b$276, >c-04,"
                ">d-00*CheckpointThree, >d-01, >d-02, >d-03, >d-04, >d-05, >d-06$130, >d-07, >d-08, >d-09, >d-10, >d-10b, >d-10c, >d-11, >space,"
                "@, b-02, &b-01, &b-03, b-04, &b-05")

eight_b: str = "00, >01, >a-00*CheckpointOne, >a-01, >a-02, >a-03, >a-04, >a-05, >b-00*CheckpointTwo, >b-01, >b-02, >b-03, >b-04, >b-05, >c-00*CheckpointThree, >c-01, >c-02, >c-03, >c-04, >c-05, >c-06, >c-08, >c-07, >space"
eight_c: str = "intro, >00, >01, >02"

farewell: str = ("intro-01-future, >intro-02-launch, ?intro-03-space, >a-00*CheckpointOne, >a-01, >a-02, >a-03, >a-04, >a-05, >b-00, >b-01, >b-02, >b-03, >b-04, >b-05, >b-06, >b-07,"
                 ">c-00*CheckpointTwo, >c-00b, >c-01, >c-02, >c-03, >d-00, &d-01, &d-02, &d-03, &d-04, &d-05, >e-00y,"
                 ">e-00z*CheckpointThree, >e-00, >e-00b, >e-01, >e-02, >e-03, >e-04, >e-05, >e-05b, >e-05c, >e-06, >e-07, >e-08,"
                 ">f-door*CheckpointFour, >f-00, >f-01, >f-02, >f-03, >f-04, >f-05, >f-06, >f-07, >f-08, >f-09, >g-00, >g-01, >g-03, >g-02, >g-04, >g-05, >g-06,"
                 ">h-00b*CheckpointFive, >h-00, >h-01, >h-02, >h-03, >h-03b, >h-04, >h-05, >h-06, >h-06b, >h-07, >h-08, >h-09, >h-10,"
                 ">i-00*CheckpointSix, >i-00b, >i-01, >i-02, >i-03, >i-04, >i-05,"
                 ">j-00*CheckpointSeven, >j-00b, >j-01, >j-02, >j-03, >j-04, >j-05, >j-06, >j-07, >j-08, >j-09, >j-10, >j-11, >j-12, >j-13, >j-14, >j-14b, >j-15, >j-16, >j-17, j-18, >j-19,"
                 "@,#c-alt-00, &>#c-alt-01, #e-00yb, h-04b")


prologue: str = "01, &-1, &0b, 1, 2, 3"

loopylagoon: str = "c-01, >c-02, >c-03, >c-04, >c-05, >c-06, >c-07, >c-08, &c-08b$2428, >c-09, >c-10, >c-1$1037, >c-12, >c-13$2140, &c-13b, >c-14, >c-15, >c-16, >c-17"
forestpath: str = "a-01, >a-02, >a-03$3, >a-04, >a-05, >a-06, >a-07, >a-08, >a-09, >a-10, >a-11$1244, >a-12, >a-13, &>a-16, >a-14, &>a-17$1634, >a-15, >a-18, >a-19$523, >a-20"
driveway: str = "00- intro, >01- Crusher, >02- Btain N' Switch, &>02B- a strwawbewwy??$682, >03- Uberjump, >04- Head Trauma, >05- Boing, >06- Bubbles, >07- Falling Cannon, &>07B- OwO whats this??$1459, >08- U Turn, >09- Fin"
azure_cavern: str = "01, >02, &02b$289, >03, >04, &04b$313, >05, >06, >07, >08"
cassettecliffs: str = "1, >2, >3, &>4, >6, >7, &8, &9, >10, >11-c, >12, @, ber4, 5"
soap: str = "01, >02, >03, >04, &04b$3286, >05, &05b$1447, >06, >07, &07b$2593, >08, >09, >10, &10b$2898, >11, &11b, >heart"
over_the_city: str = "01, >02, &Berry1$821, >03, >04, >05, &06, >07, >08, >09, >10, >11, >12, &Berry2$783, >13, >14, >15, >16, >17, @, RouteB-1$823, &RouteB-2, &RouteB-3, &RouteB-4, RouteA-2, &RouteA-1, &RouteA-3"
troposphere: str = "a_01, >a_02, >a_03, >b_01, >b_02, >b_03, >b_04, >b_05, >c_01, >c_02$101, >c_03_end"
coresaken: str = "a_01, >a_02, >a_03, >a_04, >a_05, >a_06, &b-01$112, >a_07, >a_08, &b-02$71, >a_09, >b-03, >b-04$458"
squeeze: str = "1, >2, >3, >4, >5, >6"

seeing: str = "a_01, >a_02, >a_03, >a_04, >a_05, &#a_10, >a_06, >a_07, >a_08, >a_09, >a_11$312, >#a_12"

levelSummary: str = seeing


def extractRoomName(name: str):
    return name.strip().split("*")[0].split("$")[0].replace("&", "").replace(">", "").replace("#", "")



rooms: list[str] = levelSummary.split(",")

prev_room = ""

end_reached = False

index = 0

python_room_output = []
csharp_output = []

while index < len(rooms):
    room_name = rooms[index].strip()
    if not room_name.strip() == "@":
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
        while j < len(rooms) and rooms[j].strip().startswith("&"):
            branch_rooms.append(rooms[j])
            j = j + 1
            
        next_room_index = j
        next_room = ""
        
        if next_room_index < len(rooms):
            next_room = rooms[next_room_index].strip()
            
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