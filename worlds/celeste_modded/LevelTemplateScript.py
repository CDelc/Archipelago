
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
tube_vista: str = "a01, >a02, >a02_b, >a03, &a03_s$253, >a04, >a05, >a06, &a06_s$739, >a07, >a08, >a09, &a09_s$387, &a09_b, &a09_b_s$388, >a10, >a11, >a12, &a12_s$984, >a13, &a13_b, >a14_Outro"
potential: str = "SS2-0, >SS2-1, >SS2-2, >SS2-3, >SS2-4, >SS2-5b, &SS2-6$754, >SS2-7, >HUB, >FinalChallenge, >ESCAPE, >HEART, @, WZ-0, &>WZ-1, &>WZ-2, &>WZ-3a, &>WZ-4$339, &>WZ-5a, &>WZ-Tele, Lab-0, &>Lab-1, &>Lab-2, &>Lab-3, &>Lab-4, &>Lab-5, &>Lab-6, &>Lab-7, &>Lab-Tele, Lab-5berry$731, #Lab-secret"
gift_stars: str = "Intro A, >Intro B$99, >Double Vision, >Waiting Room$633, >Timestop Intro, >Timestop Intro Again, >Stepping Stone, >Fork, >Seeded Berry$1072, &#Easter Egg Puzzle, >Staircase, >End, >End Cabin, @, Shuffle$1223, &>Feedback Loop$899"
skyline: str = "a-01, >a-02, &a-02-b, >a-04, &a-05b, >a-03, >a-05, &#a-05s, >a-06, >a-07, >a-08, &#a-08s"
strawberry: str = "a-00, >a-01z, >a-02y$822, >a-03y, >a-04z, >a-05z, &a-06z$1737, >a-07z$447, >a-08z, >a-09z, >a-11z, &a-10z$794, >a-12z$431, >a-13z"
spire: str = "a_00, >a_01$80, >a_02, >a_03$521, >a_04$624, >a_05, >a_06, >a_07$1474"
paint: str = "intro, >a-00, >a-01, >a-02, >a-03, &#a-03b, &>a-04a, >a-04b, >a-05, &>a-06b, >a-06a, &#a-06c, >a-07a, >a-08, &a-07b, &#gay, >a-09, >a-10, >b-00, &b-berry00$2675, >b-01, >b-02, >b-03, &b-berry1$471, >b-04, &b-berry2$1172, >b-05, &b-berry3$1163, >b-06, &#b-06b, >b-07, >b-08, >b-09, >b-10, >b-11, >bus, >c-intro, >c-00, >c-01, >c-02, >c-03, >c-04, >c-05, >c-06, >end, @, b-tribute"
dropzle: str = "00 - Overpass, >01 - Lockdown, >02 - Breadth, >03 - Labyrinth, &03a - Portcullis, >04 - Widdershins, &04a - Correlation, >05 - Symmetry, &>06a - Shackle, >06 - Socket, >07 - Ferry, >08 - Daedalus, &08a - Reunion, >09 - Perpendicular, >10 - Downfall, &#secret, @, 04b - Alcove"
rose: str = "q00, >q01, >q02, >q03, >q04, >q05, >q06, >q07, >q08, >q09"
treehive: str = "skeleton_00, >skeleton_01, >skeleton_02, &skeleton_02_berry$591, >skeleton_03, >skeleton_04$159, >skeleton_05, >skeleton_outro"
bhs: str = ("cp1_heartside_intro, >cp1_21_heartside_Bing_Over_Google, >cp1_20_heartside_hyperlife, >cp1_19_heartside_cellularAutomaton, >cp1_18_heartside_Eclipse,"
            ">cp2_checkpoint*Basin, >cp2-17-heartside_NotYourBadeline, >cp2-16-heartside_snas, >cp2_15_heartside_frozenflygone_a, >cp2_15_heartside_frozenflygone_b, >cp2_15_heartside_frozenflygone_c, >cp2_15_heartside_frozenflygone_d,"
            ">cp3_checkpoint*Tranquility, >cp3_14_heartside_asterisk, >cp3_13_heartside_skeleton, >cp3_12_heartside_coffe, >cp3_11_heartside_joltik,"
            ">cp4_checkpoint*Jade, >cp4_10_heartside_Hanky, >cp4_09_heartside_jadeturtle, >cp4_08_heartside_quinnigan,"
            ">cp5_checkpoint*Overgrowth, >cp5_07_heartside_voliver9, >cp5_06_heartside_CoupCritik1, >cp5_06_heartside_CoupCritik2, >cp5_06_heartside_CoupCritik3, >cp5_05_Flagpole1up_Heartside, >cp5_04_heartside_circumplex,"
            ">cp6_checkpoint*Harbor, >cp6_03_heartside_awheyaway, >cp6_02_heartside_Ceph, >cp6_03_heartside_Moss_1, >cp6_03_heartside_Moss_2, heartside_outro")
sleeping_stars: str = "a_01, &a_02, &a_03, &a_04, &a_05, >b_01, >b_02, &b_02b$214, >b_03, >b_04, >b_05"
square_circle: str = "a_01, >a-02$1386, >a_02.5, >a_03, &b_01$447, >a_04, &b_02$566, >a_05, >a_06, &b_03$1139, >a_07, >a_08, &b_04$594, >a_09, >a_10, >outro, #hmmmm, #uwu"
frosted: str = "a1, >a1.5v2, >a2v2, >a3v2, >a4v2, >a5_, >a6v2, &r_00v2$4230, >pushupv2, >reboundv2, >a9v2, >a_10v2, &r_01v2, >downmoveblockv2, >end_but_for_real_this_time"
blue: str = "a_01, >a_02, >a_03$582, >a_04$1107, >a_05$585, >a_06, >a_07, >a_08, >a_09"
vertigo: str = "Evilleafy-00, >Evilleafy-01, >Evilleafy-02, >Evilleafy-03a, >Evilleafy-04a, >Evilleafy-06, >Evilleafy-07, >Evilleafy-04, >Evilleafy-08b, >Evilleafy-09, >Evilleafy-10"
EATGIRL: str = "A-01, >A-02, >A-03, >A-04, >A-05, &A-05b$120, >A-06, >A-07, &A-07b$328, >A-08, >A-09"
honeyzip: str = "startroom, >r1, >r2, >r3, >rhub, &r4, &r5, &r6, &r7, &r8, >r9$500, &r9sb$1242, >endroom, &>#endroomsecret, @, r6sb$141"
temple: str = "a-01, >a-02, >a-03, >a-04, >b-01, >c-01$3054, >c-02, @, b-05, &b-06$2196, &b-07, b-02, &b-03$3253, &b-04$3261"
infil: str = "btd-00, >btd-02, &btd-02b$827, &btd-02c$839, >btd-02a, >btd-03, >btd-04, &#btd-04a, >btd-05, &btd-05a$569, >btd-06, >btd-07, >btd-09, >btd-20, &btd-20a$806, >btd-21, >btd-30, >btd-31, >btd-33, >btd-35$755, >btd-42, >gg, @, btd-12, &btd-13, &btd-11"
nautica: str = "LegS-0, >LegS-1, >LegS-2, >LegS-B1$1313, >LegS-3, &#LegS-Intermediate, >LegS-4, >LegS-B2$795, >LegS-5, >LegS-6, >LegS-7, @, #LegS-CR"
fifthdim: str = "A00, >A01, >A02, >A03, >A04, >A05, >A06, >A07, >A08, >A09, >A10, >A11, >A12"
monsoon: str = "Intro, >1, >2, &2b$1285, >3, >4, >5, &5b, >6, >outro, >outrob"
lowg: str = "1, >2, >3, >4$1837, >5, >5b$3631, >6$2324, >7"
towerint: str = "lvl00, >lvl01$164, >lvl02$476, >lvl03, >lvl04$574, >lvl05, >lvl06, >lvl07"
puffer: str = "RG2-0, >RG2-1, >RG2-2, >RG2-3, >RG2-4, &RG2-4-S1, &RG2-4-S2, >RG2-5, &RG2-5-S, >RG2-6, >RG2-7, >RG2-8, >RG2-9, >RG2-End, @, RG2-huh"
seasoup: str = "soup-1, >soup-2, >soup-3$139, >soup-4, &soup-4b$2022, >soup-5, &soup-5b$879, >soup-6, &soup-6b$878, >soup-7$2312"
construction: str = "a-001, &a-000$1410, >a-002, >a-003, >a-004, >a-005, >a-006, >a-007, >a-008, >a-009, &a-011$1912, >a-010, >a-012, >a-013, @, a-000S"
pointlessmachines: str = "01, >02, >03, &03-berry, >04, >05, >06, &06-berry, >07, >08, >09"
ihs: str = ("cp1-0-intro, >cp1-1-liero, >cp1-2-pixelator, >cp1-3-Evilleafy, >cp1-4-ezel,"
            ">cp2-0-Cp, >cp2-1-SpoopySoup, >cp2-2-dooshii, >cp2-3-glowwoomii, >cp2-4-ice, >cp2-5-bryse0n,"
            ">cp3-0-Cp, >cp3-1-Arphimigon, >cp3-2-LegS, >cp3-3-Jems, >cp3-4-vitellary, >cp3-5-RG2,"
            ">cp4-0-Cp, >cp4-1-Emik, >cp4-2-thebreadstick1, >cp4-3-Luma, >cp4-4-Marlin, >cp4-5-Heart")
sands: str = "a-00, >a-01, >a-02, >a-03, >a-04-bis, >a-05, >a-06, &a-strawberry$510, >b-01$195, &b-01-view, >b-02, >b-03, >mini-hearth$4028, &b-strawberry"
jellysanctum: str = "intro, >1, >2, >3, &berry1$92, >reverseTutorial, >4, >5, >outro"
toggletheory: str = "intro, >a-1, >a-2, &berry0$3160, >a-3, &berry1$623, >a-4, >bhop, >a-5, &berry2$1110, >a-6, >epilogue, >heart, &#outlook"
slime: str = "a_00-Worldwaker2, >a_01-Gala, >a_02-Gala, >a_03-Oppen_heimer$986, >a_04-Gala, &berry-01-Oppen$2567, >a_05-TiltTheStars, >a_06-TiltTheStars, >a_07-TiltTheStars$2684, >a_08-TiltTheStars, >heart_room"
superstructure: str = "start, >tutorial-1, >goldian-1, >aiden-2, >goldian-3, >goldian-4, >tutorial-2, >goldian-5, &goldian-berry$2200, >goldian-6, >goldian-7, >end"
laserlab: str = "a_01, >a_02, >a_03, >a_04, >a_05, >a_06, &a_06b, >a_07"
starryruin: str = "1, >2, >3, >4, >5, >6, >7, >8, >9, >10"
towerxvi: str = "1, >2, >3, >4, >5, >6, >7"
starlightstation: str = "a0, &#a-secret, >a1, >a2, &a-berry$4332, >a3, >b1, >b2, >b3, >b4, &b-berry$7539, >b5, >65, >b7, >brys1, >brys2, >brys3, >brys4, &brys-berry$7540"
tectonic: str = "a-01, >a-02, >a-03, >a-04$1114, >a-05intro, &transition, >a-05, >a-07, >a-06, @, Berry 1$895"
goldendawn: str = "A0, >A2, &A2_v2$3574, >A4, >A5, &A5_v2$239, >Brys2-2-2, &A6_v2-flip-2$4103, >A6, >A7"
duskcity: str = "a-01, &#b-01, >a-02, >a-03, >a-04, >a-05, >a-06, >a-07, >a-08, >a-09, >a-10"
skateboard: str = "a00, >a01, >a02, >a03, >a04, >a05, >a06, >a07, &a07b, >a08, >a09, >a10, &a10b"
synapse: str = "intro_fall, >intro_a1, >a1, >a2, >a3, >a4, >a5, >b1, &b1_b$3951, >b2, >b3, >c1"
undergrowth: str = "01-a, >02-a, >03-a$879, >05-a$2573, >06-a$2886, &#06-s1, &06-b$3377, >07-a, >08-a, @, 04-a, &04-s1$1659"
lostwoods: str = "oppen_intro, oppen_1a, oppen_berry$647"
aotc: str = "BR-00, >BR-02, >BR-01, >BR-08, >BR-03, >BR-04, >BR-07, >BR-05, >BR-Outro, &BR-Extra$866"
lab: str = "start-01-Radley, >start-02-Radley, >start-03-Radley/Worldwaker2, >start-04-Radley, >start-05-TiltTheStars, >hub, >cross-01-Worldwaker2, >cross-02-TiltTheStars, >cross-03-TiltTheStars$86, >evade-01-Quantum, >evade-02b-Quantum$87, >evade-02-TiltTheStars, >evade-03-Worldwaker2, >move-01-TiltTheStars, >move-02-Worldwaker2, >move-02b-Quantum$9, >escape-01-Worldwaker2, >escape-02-Worldwaker2, >escape-03-Worldwaker2, >start-00-Radley, >end_HideInMap"
belated: str = "1-intro, >1-a, >1-b, >1-c, >1-e, >1-f, &1-d, >1-g, >1-h, >2-a, >2-b, >2-c, >2-d, >2-secret :D"
thinking: str = "a-01, >a-02, >a-04, >a-05, >a-06$1384, >a-07, >a-08, &a-10$401, >a-09, >a-11, &a-12$723, >a-13"
bee: str = "intro_v1, >intro_v2, >a-01, >a-02, >a-03, >a-04, >a-05, >a-06, &secret-02, >a-07, >a-08, >badeline_v2, >mini_heart_room, @, secret-02"
java: str = "0b, >0, >1, >1b, >2, >2b, >3, >3b, >4, >4b, >5, >6, &#6e"
rightside: str = "intro_SJ$374, >Vamp_2, >Vamp_3, >Vamp_4, >Vamp_5, >Vamp_6$2459$2136, >Vamp_7, >Vamp_8, >Vamp_9, >Vamp_Final"
callofvoid: str = "viv0, >viv1, >viv2, &viv2b$654, >viv3, >viv3x, >viv4, >viv5, &viv5b$1742, >viv5x, >viv6, >viv7, &viv7b$2006, >viv8$94, >vivEnd, >vivEB$2760, >#vivEB_, >#_Endgame, >#vivBonus"
raindrops: str = "1, &1B$264, >2, &2B, >3, >4, >5, >6, >7, >8, &9"
mango: str = ("Start, >heartside_oppen_intro, >heartside_oppen_a, &heartside_oppen_b, &heartside_oppen_c, >heartside_Worldwaker2, >heartside_TiltTheStars, >heartside_Galaksyz, >heartside_mmm,"
              ">Crest*CheckpointOne, >heartside_MousseMoose, >heartside_Meario, >heartside_YaGrillRobib, >heartside_maladroit, >heartside_pugroy,"
              ">Ravine*CheckpointTwo, >heartside_astraxel, >heartside_Tortoise, >heartside_Tortoise_B, >heartside_bluexans, >heartside_Vamp, >heartside_Julia,"
              ">Aquifer*CheckpointThree, >heartside_sp1029, >heartside_hennyburgr, >heartside_Indecx, >heartside_Nic, >heartside_Ian,"
              ">Landing*CheckpointFour, >heartside_citrea, >heartside_RadleyMcTuneston, >heartside_Goldian, >heartside_jolly, >heartside_Viv, >Fin")
direction: str = "Ru_and_AV_and_Zucchini_Are_Cool, >Agent_00, >Agent_00a, >Agent_01, >Agent_02, >Agent_03, >Agent_04, &Agent_04b$383, >Agent_05, >Agent_06, >Agent_07"
battery: str = "a-01, >a-02, >a-03, >a-04, >a-05, >a-06, >a-07, &a-08$2295"
skyline: str = "INTRO1, >INTRO2, >a01, >a01b, >a02, >a03, >a04, >a05, >a06new, >a07, &a07b, >a08outro"
chromatic: str = "a-00, >a-01, >a-02, >a-03, >a-04, >a-05, >a-06, >a-07, >a-08, >a-09, >a-10, >a-11, >a-12, >a-13"
fortress: str = "00-intro, >00-intro-cutscene, >01, >03, >05-hub, >06-crossroad, &06-berry$1635, >07, &07-berry$125, >08, >09, >11, >99-end, @, 07-berry-2$2055"
coreproblem: str = "a-01, >a-02, >a-03, >a-04, &a-04b$980, >a-05, >a-06, &a-06b$1664, >a-07, >a-08, >a-09, &a-09b$2912, >a-10, >a-11"
psycho: str = "a-start, &#s-Path of Plane, >a-00, >a-01, >a-02, &#s-Flushed Down, >a-03, &a-03x$570, >a-04, >a-05, >a-06, &#s-Swamp Ascent, >a-07, >a-08, &a-08x$1876, >a-09, >a-10, &a-10x$2917, >a-end, >#a-end2, >#s-True Ending, >s-Graveyard, @, #s-Water Splash, #s-Shrek Swamp"
khutara: str = "DanTKO_Intro, &#DanTKO_Monolith_1, &#DanTKO_Plane, >DanTKO_01, >DanTKO_02, >DanTKO_blueTutorial_2, >DanTKO_03, >DanTKO_04, >DanTKO_05, >DanTKO_06, >DanTKO_06b, &DanTKO_Berry01$2078, >DanTKO_07, >DanTKO_08, >DanTKO_09, &DanTKO_Berry02$331, >DanTKO_Outro, @, Aperture_Mountain Relic, >&Aperture_Mountain Relic_EXIT"
linn: str = "a-00-start, &a-00a, >a-01, &a-01_berry$1575, >a-02, >a-03, >a-04, >a-05, >a-06, >a-07, &a-07_berry$2751, >a-08, &a-08_berry$3479, >a-09, >a-10-end, >a-10_berry$3513, >#a-10a, @, #a-00c, &#a-00b, &#a-00y"
clock: str = "a-00, >a-01, >a-02, >a-03, >a-04, >a-05, &a-05b$2707, >a-06, >a-07, &a-07b$2134, &#secret, >a-08, >a-09, &a-09b$13047"
plasma: str = "a1, >a2, >a3, >a4, >a5, >a6, >a7, >a8, &>a9, b1$2100, bones_room"
hollow: str = "1, >2, >3, >4, >5, >6$334, &berry, >7, >8, >9, >10"

hydro: str = "a01, &#a02, >a04, >a05, >a06, >a07$181, >a08, >a09, >a10, &a10b$1187, >a12, &a12b$129, >a14, >a15, @,#a03"

levelSummary: str = hydro


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
            room_args.append("easter_egg=True")
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