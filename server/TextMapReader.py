# -*- coding: utf-8 -*-

import logging
from datatables.MapsTable import MapsTable
from model.map.V1Map import V1Map

MAP_INFO = ((0, 32256, 32767, 32768, 33279),
            (1, 32640, 32767, 32768, 32895),
            (2, 32640, 32831, 32768, 32895),
            (3, 32640, 32767, 32768, 32831),
            (4, 32384, 34303, 32064, 33535),
            (5, 32704, 32767, 32768, 32831),
            (6, 32704, 32767, 32768, 32831),
            (7, 32704, 32831, 32704, 32831),
            (8, 32704, 32831, 32704, 32831),
            (9, 32704, 32831, 32704, 32831),
            (10, 32704, 32831, 32704, 32831),
            (11, 32704, 32831, 32704, 32831),
            (12, 32704, 32831, 32704, 32831),
            (13, 32704, 32831, 32704, 32831),
            (14, 32512, 33023, 32768, 32831),
            (15, 32704, 32767, 32768, 32831),
            (16, 32704, 32767, 32768, 32831),
            (17, 32704, 32767, 32768, 32831),
            (18, 32704, 32767, 32768, 32831),
            (19, 32704, 32831, 32704, 32831),
            (20, 32704, 32831, 32704, 32831),
            (21, 32704, 32831, 32704, 32831),
            (22, 32704, 32831, 32704, 32831),
            (23, 32704, 32831, 32704, 32831),
            (24, 32704, 32831, 32704, 32831),
            (25, 32704, 32831, 32704, 32831),
            (26, 32704, 32831, 32704, 32831),
            (27, 32704, 32831, 32704, 32831),
            (28, 32704, 32831, 32704, 32831),
            (29, 32704, 32767, 32768, 32831),
            (30, 32704, 32831, 32704, 32831),
            (31, 32704, 32831, 32704, 32831),
            (32, 32640, 32767, 32768, 32895),
            (33, 32640, 32767, 32768, 32895),
            (34, 32704, 32767, 32768, 32831),
            (35, 32640, 32767, 32768, 32895),
            (36, 32640, 32767, 32768, 32895),
            (37, 32640, 32767, 32768, 32895),
            (38, 32704, 32767, 32768, 32831),
            (39, 32704, 32767, 32768, 32831),
            (40, 32704, 32767, 32768, 32831),
            (41, 32704, 32767, 32768, 32831),
            (43, 32704, 32831, 32704, 32831),
            (44, 32704, 32831, 32704, 32831),
            (45, 32704, 32831, 32704, 32831),
            (46, 32704, 32831, 32704, 32831),
            (47, 32704, 32831, 32704, 32831),
            (48, 32704, 32831, 32704, 32831),
            (49, 32704, 32831, 32704, 32831),
            (50, 32704, 32831, 32704, 32831),
            (51, 32640, 32831, 32704, 32895),
            (52, 32640, 32767, 32768, 32895),
            (53, 32704, 32831, 32704, 32831),
            (54, 32704, 32831, 32704, 32831),
            (55, 32704, 32767, 32704, 32895),
            (56, 32704, 32831, 32704, 32831),
            (57, 32576, 33023, 32512, 32959),
            (58, 32512, 32831, 32704, 33023),
            (59, 32640, 32767, 32768, 32895),
            (60, 32640, 32767, 32768, 32895),
            (61, 32640, 32767, 32768, 32895),
            (62, 32640, 32767, 32768, 32895),
            (63, 32576, 32895, 32640, 32959),
            (64, 32512, 32639, 32768, 32895),
            (65, 32704, 32831, 32768, 32895),
            (66, 32704, 32895, 32768, 32959),
            (67, 32640, 32831, 32704, 32895),
            (68, 32576, 33023, 32512, 32959),
            (69, 32512, 32831, 32704, 33023),
            (70, 32576, 33023, 32640, 33087),
            (72, 32704, 32895, 32768, 32895),
            (73, 32704, 32895, 32704, 32895),
            (74, 32704, 32895, 32768, 32959),
            (75, 32704, 32831, 32768, 32959),
            (76, 32704, 32831, 32768, 32895),
            (77, 32704, 32831, 32768, 32895),
            (78, 32832, 32959, 32704, 32831),
            (79, 32704, 32831, 32768, 32895),
            (80, 32704, 32831, 32768, 32895),
            (81, 32704, 32831, 32768, 32895),
            (82, 32640, 32767, 32768, 32895),
            (83, 32704, 32767, 32768, 32831),
            (84, 32704, 32767, 32768, 32831),
            (85, 32576, 32767, 32704, 32895),
            (86, 32768, 32959, 32704, 32895),
            (87, 32704, 32767, 32768, 32831),
            (88, 33472, 33535, 32704, 32767),
            (89, 32640, 32767, 32832, 32959),
            (90, 32640, 32767, 32832, 32959),
            (91, 32640, 32767, 32832, 32959),
            (92, 32640, 32767, 32832, 32959),
            (93, 32640, 32767, 32832, 32959),
            (94, 32640, 32767, 32832, 32959),
            (95, 32640, 32767, 32832, 32959),
            (96, 32640, 32767, 32832, 32959),
            (97, 32640, 32767, 32832, 32959),
            (98, 32640, 32767, 32832, 32959),
            (99, 32704, 32767, 32768, 32831),
            (101, 32704, 32895, 32704, 32895),
            (102, 32704, 32895, 32704, 32895),
            (103, 32704, 32895, 32704, 32895),
            (104, 32576, 32767, 32768, 32959),
            (105, 32576, 32767, 32768, 32959),
            (106, 33728, 33855, 32832, 32895),
            (107, 32576, 32767, 32768, 32959),
            (108, 32576, 32767, 32768, 32959),
            (109, 32576, 32767, 32768, 32959),
            (110, 32704, 32895, 32704, 32895),
            (111, 32576, 32767, 32768, 32959),
            (112, 32704, 32895, 32704, 32895),
            (113, 32704, 32895, 32704, 32895),
            (114, 32576, 32767, 32768, 32959),
            (115, 32576, 32767, 32768, 32959),
            (116, 32704, 32831, 32832, 32895),
            (117, 32576, 32767, 32768, 32959),
            (118, 32576, 32767, 32768, 32959),
            (119, 32576, 32767, 32768, 32959),
            (120, 32704, 32895, 32704, 32895),
            (121, 32576, 32767, 32768, 32959),
            (122, 32704, 32895, 32704, 32895),
            (123, 32704, 32895, 32704, 32895),
            (124, 32576, 32767, 32768, 32959),
            (125, 32576, 32767, 32768, 32959),
            (126, 32704, 32831, 32832, 32895),
            (127, 32576, 32767, 32768, 32959),
            (128, 32576, 32767, 32768, 32959),
            (129, 32576, 32767, 32768, 32959),
            (130, 32704, 32895, 32704, 32895),
            (131, 32576, 32767, 32768, 32959),
            (132, 32704, 32895, 32704, 32895),
            (133, 32704, 32895, 32704, 32895),
            (134, 32576, 32767, 32768, 32959),
            (135, 32576, 32767, 32768, 32959),
            (136, 32704, 32831, 32832, 32895),
            (137, 32576, 32767, 32768, 32959),
            (138, 32576, 32767, 32768, 32959),
            (139, 32576, 32767, 32768, 32959),
            (140, 32704, 32895, 32704, 32895),
            (141, 32576, 32767, 32768, 32959),
            (142, 32704, 32895, 32704, 32895),
            (143, 32704, 32895, 32704, 32895),
            (144, 32576, 32767, 32768, 32959),
            (145, 32576, 32767, 32768, 32959),
            (146, 32704, 32831, 32832, 32895),
            (147, 32576, 32767, 32768, 32959),
            (148, 32576, 32767, 32768, 32959),
            (149, 32576, 32767, 32768, 32959),
            (150, 32704, 32895, 32704, 32895),
            (151, 32576, 32767, 32768, 32959),
            (152, 32576, 32767, 32768, 32959),
            (153, 32576, 32767, 32768, 32959),
            (154, 32704, 32895, 32704, 32895),
            (155, 32704, 32895, 32704, 32895),
            (156, 32704, 32831, 32768, 32831),
            (157, 32576, 32767, 32768, 32959),
            (158, 32576, 32767, 32768, 32959),
            (159, 32576, 32767, 32768, 32959),
            (160, 32576, 32767, 32768, 32959),
            (161, 32576, 32767, 32768, 32959),
            (162, 32576, 32767, 32768, 32959),
            (163, 32576, 32767, 32768, 32959),
            (164, 32704, 32895, 32704, 32895),
            (165, 32704, 32895, 32704, 32895),
            (166, 32704, 32831, 32768, 32831),
            (167, 32576, 32767, 32768, 32959),
            (168, 32576, 32767, 32768, 32959),
            (169, 32576, 32767, 32768, 32959),
            (170, 32576, 32767, 32768, 32959),
            (171, 32576, 32767, 32768, 32959),
            (172, 32576, 32767, 32768, 32959),
            (173, 32576, 32767, 32768, 32959),
            (174, 32704, 32895, 32704, 32895),
            (175, 32704, 32895, 32704, 32895),
            (176, 32704, 32831, 32768, 32831),
            (177, 32576, 32767, 32768, 32959),
            (178, 32576, 32767, 32768, 32959),
            (179, 32576, 32767, 32768, 32959),
            (180, 32576, 32767, 32768, 32959),
            (181, 32576, 32767, 32768, 32959),
            (182, 32576, 32767, 32768, 32959),
            (183, 32576, 32767, 32768, 32959),
            (184, 32704, 32895, 32704, 32895),
            (185, 32704, 32895, 32704, 32895),
            (186, 32704, 32831, 32768, 32831),
            (187, 32576, 32767, 32768, 32959),
            (188, 32576, 32767, 32768, 32959),
            (189, 32576, 32767, 32768, 32959),
            (190, 32576, 32767, 32768, 32959),
            (191, 32576, 32767, 32768, 32959),
            (192, 32576, 32767, 32768, 32959),
            (193, 32576, 32767, 32768, 32959),
            (194, 32704, 32895, 32704, 32895),
            (195, 32704, 32895, 32704, 32895),
            (196, 32704, 32831, 32768, 32831),
            (197, 32576, 32767, 32768, 32959),
            (198, 32576, 32767, 32768, 32959),
            (199, 32576, 32767, 32768, 32959),
            (200, 32576, 32831, 32768, 33023),
            (201, 32768, 32959, 32768, 32959),
            (202, 32640, 32767, 32768, 32895),
            (203, 32640, 32767, 32768, 32895),
            (204, 32640, 32767, 32768, 32895),
            (205, 32640, 32767, 32768, 32895),
            (206, 32640, 32767, 32768, 32895),
            (207, 32640, 32767, 32768, 32895),
            (208, 32640, 32767, 32768, 32895),
            (209, 32640, 32767, 32768, 32895),
            (210, 32640, 32767, 32768, 32895),
            (211, 32640, 32767, 32768, 32895),
            (213, 32704, 32767, 32768, 32831),
            (217, 32640, 32767, 32768, 32831),
            (221, 32704, 32831, 32704, 32831),
            (237, 32704, 32767, 32768, 32831),
            (240, 32640, 32767, 33024, 33151),
            (241, 32704, 32831, 32832, 32959),
            (242, 32704, 32831, 32896, 33023),
            (243, 32640, 32767, 32832, 33023),
            (244, 32704, 33023, 32768, 33087),
            (248, 32704, 32831, 32768, 32895),
            (249, 32704, 32831, 32832, 32895),
            (250, 32704, 32831, 32768, 32895),
            (251, 32768, 32831, 32768, 32831),
            (252, 32576, 32767, 32832, 32895),
            (253, 32704, 32831, 32832, 33023),
            (254, 32576, 32767, 32768, 32959),
            (255, 32640, 32831, 32768, 32895),
            (256, 32640, 32895, 32768, 33023),
            (257, 32640, 32831, 32768, 32831),
            (258, 32640, 32831, 32768, 33151),
            (259, 32704, 32767, 32768, 32959),
            (300, 32832, 32959, 32448, 32639),
            (301, 32640, 32767, 32768, 32959),
            (302, 32704, 32767, 32832, 32895),
            (303, 32576, 32895, 32576, 32895),
            (304, 32576, 32959, 32768, 33023),
            (305, 32704, 32767, 32768, 32831),
            (306, 32512, 32767, 32768, 32959),
            (307, 32704, 32959, 32768, 32959),
            (308, 32704, 33023, 32768, 32959),
            (309, 32704, 33087, 32768, 32959),
            (310, 32704, 32895, 32768, 32959),
            (320, 32704, 33087, 32768, 33023),
            (330, 32704, 32767, 32832, 33023),
            (340, 32704, 32831, 32768, 32895),
            (350, 32640, 32767, 32768, 32895),
            (360, 32704, 32767, 32768, 32831),
            (370, 32704, 32767, 32768, 32831),
            (400, 32512, 33023, 32576, 33023),
            (401, 32704, 32831, 32768, 32895),
            (410, 32704, 32959, 32768, 33023),
            (420, 32704, 32831, 32832, 33087),
            (430, 32704, 32959, 32768, 33023),
            (440, 32256, 32767, 32768, 33279),
            (441, 32640, 32831, 32704, 32895),
            (442, 32704, 32895, 32704, 32895),
            (443, 32704, 32895, 32704, 32895),
            (444, 32704, 32767, 32768, 32831),
            (445, 32704, 32831, 32832, 32895),
            (446, 32704, 32767, 32768, 32831),
            (447, 32704, 32767, 32768, 32831),
            (450, 32640, 32831, 32768, 32959),
            (451, 32704, 32831, 32768, 32895),
            (452, 32704, 32831, 32768, 32895),
            (453, 32704, 32895, 32704, 32895),
            (454, 32704, 32831, 32768, 32895),
            (455, 32704, 32831, 32768, 32895),
            (456, 32704, 32831, 32768, 32895),
            (457, 32640, 32703, 32832, 32895),
            (460, 32704, 32831, 32768, 32895),
            (461, 32640, 32895, 32768, 32895),
            (462, 32640, 32831, 32768, 32895),
            (463, 32704, 32831, 32768, 32895),
            (464, 32704, 32831, 32768, 32895),
            (465, 32704, 32831, 32768, 32895),
            (466, 32704, 32831, 32768, 32895),
            (467, 32640, 32703, 32832, 32895),
            (468, 32640, 32703, 32832, 32895),
            (470, 32704, 32895, 32768, 32895),
            (471, 32704, 32831, 32768, 32895),
            (472, 32704, 32831, 32768, 32831),
            (473, 32704, 32959, 32768, 32895),
            (474, 32704, 32831, 32768, 32895),
            (475, 32640, 32831, 32768, 32895),
            (476, 32704, 32831, 32768, 32895),
            (477, 32704, 32831, 32768, 32895),
            (478, 32704, 32767, 32768, 32895),
            (480, 32640, 32895, 32768, 33023),
            (481, 32704, 32767, 32768, 32895),
            (482, 32640, 32831, 32704, 32895),
            (483, 32704, 32831, 32768, 32959),
            (484, 32704, 32831, 32768, 32895),
            (490, 32640, 32767, 32768, 32895),
            (491, 32640, 32767, 32704, 32895),
            (492, 32768, 32895, 32768, 32895),
            (493, 32704, 32831, 32704, 32831),
            (494, 32768, 32895, 32704, 32831),
            (495, 32704, 32831, 32768, 32895),
            (496, 32768, 32895, 32768, 32895),
            (500, 32704, 32767, 32768, 32831),
            (501, 32832, 32895, 32576, 32703),
            (502, 32832, 32895, 32576, 32703),
            (503, 32832, 32895, 32576, 32703),
            (504, 32832, 32895, 32576, 32703),
            (505, 32832, 32895, 32576, 32703),
            (506, 32832, 32895, 32576, 32703),
            (507, 32704, 33023, 32768, 32959),
            (508, 32768, 32895, 33088, 33215),
            (509, 32704, 32767, 32768, 32831),
            (511, 32832, 32895, 32576, 32703),
            (512, 32832, 32895, 32576, 32703),
            (513, 32832, 32895, 32576, 32703),
            (514, 32832, 32895, 32576, 32703),
            (515, 32832, 32895, 32576, 32703),
            (516, 32832, 32895, 32576, 32703),
            (521, 32640, 32767, 32896, 33023),
            (522, 32640, 32767, 32832, 32959),
            (523, 32640, 32767, 32832, 32959),
            (524, 32640, 32767, 32832, 32959),
            (530, 32704, 32895, 32768, 32895),
            (531, 32704, 32895, 32704, 32895),
            (532, 32704, 32895, 32768, 32895),
            (533, 32704, 32895, 32768, 32959),
            (534, 32704, 32959, 32768, 32895),
            (535, 32576, 32895, 32704, 33023),
            (536, 32704, 32767, 32768, 32831),
            (541, 32704, 32767, 32768, 32895),
            (542, 32704, 32767, 32768, 32895),
            (543, 32704, 32895, 32704, 32895),
            (550, 32384, 32895, 32640, 33151),
            (551, 32640, 32767, 32768, 32895),
            (552, 32704, 32767, 32768, 32895),
            (553, 32704, 32831, 32768, 32895),
            (554, 32704, 32831, 32768, 32895),
            (555, 32704, 32767, 32768, 32895),
            (556, 32704, 32831, 32768, 32895),
            (557, 32704, 32831, 32768, 32895),
            (558, 32704, 33215, 32768, 33279),
            (600, 32704, 32831, 32768, 32831),
            (601, 32704, 32895, 32768, 32895),
            (602, 32640, 32767, 32768, 32895),
            (603, 32640, 32767, 32768, 32895),
            (604, 32768, 32895, 32768, 32895),
            (605, 32768, 32895, 32768, 32895),
            (606, 32704, 32831, 32768, 32895),
            (607, 32704, 32831, 32768, 32895),
            (608, 32640, 32767, 32832, 32959),
            (610, 32704, 32831, 32768, 32895),
            (611, 32704, 32831, 32704, 32831),
            (612, 32704, 32831, 32768, 32895),
            (666, 32640, 32831, 32704, 32895),
            (701, 32640, 32959, 32576, 32895),
            (777, 32512, 32767, 32832, 33087),
            (778, 32704, 32959, 32640, 32959),
            (779, 32832, 32959, 32704, 32831),
            (780, 32576, 32831, 32704, 33087),
            (781, 32704, 33023, 32704, 32895),
            (782, 32704, 32831, 32768, 32895),
            (783, 32768, 33279, 32640, 32895),
            (784, 32704, 32831, 32768, 32895),
            (997, 32704, 32767, 32768, 32831),
            (998, 32704, 32767, 32768, 32831),
            (1000, 32704, 32895, 32768, 32959),
            (1001, 32704, 32895, 32768, 32959),
            (2000, 32704, 32895, 32832, 33023),
            (2001, 32640, 32831, 32704, 32895),
            (2002, 32704, 32831, 32768, 32895),
            (2003, 32704, 32895, 32768, 32959),
            (2004, 32704, 32895, 32768, 32895),
            (4941, 32768, 32895, 32704, 32831),
            (5001, 32704, 32831, 32704, 32831),
            (5002, 32704, 32831, 32704, 32831),
            (5003, 32704, 32831, 32704, 32831),
            (5004, 32704, 32831, 32704, 32831),
            (5005, 32704, 32831, 32704, 32831),
            (5006, 32704, 32831, 32704, 32831),
            (5007, 32704, 32831, 32704, 32831),
            (5008, 32704, 32831, 32704, 32831),
            (5009, 32704, 32831, 32704, 32831),
            (5010, 32704, 32831, 32704, 32831),
            (5011, 32704, 32831, 32704, 32831),
            (5012, 32704, 32831, 32704, 32831),
            (5013, 32704, 32831, 32704, 32831),
            (5014, 32704, 32831, 32704, 32831),
            (5015, 32704, 32831, 32704, 32831),
            (5016, 32704, 32831, 32704, 32831),
            (5017, 32704, 32831, 32704, 32831),
            (5018, 32704, 32831, 32704, 32831),
            (5019, 32704, 32831, 32704, 32831),
            (5020, 32704, 32831, 32704, 32831),
            (5021, 32704, 32831, 32704, 32831),
            (5022, 32704, 32831, 32704, 32831),
            (5023, 32704, 32831, 32704, 32831),
            (5024, 32704, 32831, 32704, 32831),
            (5025, 32704, 32831, 32704, 32831),
            (5026, 32704, 32831, 32704, 32831),
            (5027, 32704, 32831, 32704, 32831),
            (5028, 32704, 32831, 32704, 32831),
            (5029, 32704, 32831, 32704, 32831),
            (5030, 32704, 32831, 32704, 32831),
            (5031, 32704, 32831, 32704, 32831),
            (5032, 32704, 32831, 32704, 32831),
            (5033, 32704, 32831, 32704, 32831),
            (5034, 32704, 32831, 32704, 32831),
            (5035, 32704, 32831, 32704, 32831),
            (5036, 32704, 32831, 32704, 32831),
            (5037, 32704, 32831, 32704, 32831),
            (5038, 32704, 32831, 32704, 32831),
            (5039, 32704, 32831, 32704, 32831),
            (5040, 32704, 32831, 32704, 32831),
            (5041, 32704, 32831, 32704, 32831),
            (5042, 32704, 32831, 32704, 32831),
            (5043, 32704, 32831, 32704, 32831),
            (5044, 32704, 32831, 32704, 32831),
            (5045, 32704, 32831, 32704, 32831),
            (5046, 32704, 32831, 32704, 32831),
            (5047, 32704, 32831, 32704, 32831),
            (5048, 32704, 32831, 32704, 32831),
            (5049, 32704, 32831, 32704, 32831),
            (5050, 32704, 32831, 32704, 32831),
            (5051, 32704, 32831, 32704, 32831),
            (5052, 32704, 32831, 32704, 32831),
            (5053, 32704, 32831, 32704, 32831),
            (5054, 32704, 32831, 32704, 32831),
            (5055, 32704, 32831, 32704, 32831),
            (5056, 32704, 32831, 32704, 32831),
            (5057, 32704, 32831, 32704, 32831),
            (5058, 32704, 32831, 32704, 32831),
            (5059, 32704, 32831, 32704, 32831),
            (5060, 32704, 32831, 32704, 32831),
            (5061, 32704, 32831, 32704, 32831),
            (5062, 32704, 32831, 32704, 32831),
            (5063, 32704, 32831, 32704, 32831),
            (5064, 32704, 32831, 32704, 32831),
            (5065, 32704, 32831, 32704, 32831),
            (5066, 32704, 32831, 32704, 32831),
            (5067, 32704, 32831, 32704, 32831),
            (5068, 32704, 32831, 32768, 32895),
            (5069, 32704, 32831, 32768, 32895),
            (5070, 32704, 32831, 32768, 32895),
            (5071, 32704, 32831, 32768, 32895),
            (5072, 32704, 32831, 32768, 32895),
            (5073, 32704, 32831, 32768, 32895),
            (5074, 32704, 32831, 32768, 32895),
            (5075, 32704, 32831, 32768, 32895),
            (5076, 32704, 32831, 32768, 32895),
            (5077, 32704, 32831, 32768, 32895),
            (5078, 32704, 32831, 32768, 32895),
            (5079, 32704, 32831, 32768, 32895),
            (5080, 32704, 32831, 32768, 32895),
            (5081, 32704, 32831, 32768, 32895),
            (5082, 32704, 32831, 32768, 32895),
            (5083, 32704, 32831, 32768, 32895),
            (5084, 32704, 32831, 32768, 32895),
            (5085, 32704, 32831, 32768, 32895),
            (5086, 32704, 32831, 32768, 32895),
            (5087, 32704, 32831, 32768, 32895),
            (5088, 32704, 32831, 32768, 32895),
            (5089, 32704, 32831, 32768, 32895),
            (5090, 32704, 32831, 32768, 32895),
            (5091, 32704, 32831, 32768, 32895),
            (5092, 32704, 32831, 32768, 32895),
            (5093, 32704, 32831, 32768, 32895),
            (5094, 32704, 32831, 32768, 32895),
            (5095, 32704, 32831, 32768, 32895),
            (5096, 32704, 32831, 32768, 32895),
            (5097, 32704, 32831, 32768, 32895),
            (5098, 32704, 32831, 32768, 32895),
            (5099, 32704, 32831, 32768, 32895),
            (5100, 32704, 32831, 32768, 32895),
            (5101, 32704, 32831, 32768, 32895),
            (5102, 32704, 32831, 32768, 32895),
            (5103, 32704, 32831, 32768, 32895),
            (5104, 32704, 32831, 32768, 32895),
            (5105, 32704, 32831, 32768, 32895),
            (5106, 32704, 32831, 32768, 32895),
            (5107, 32704, 32831, 32768, 32895),
            (5108, 32704, 32831, 32768, 32895),
            (5109, 32704, 32831, 32768, 32895),
            (5110, 32704, 32831, 32768, 32895),
            (5111, 32704, 32831, 32768, 32895),
            (5112, 32704, 32831, 32768, 32895),
            (5113, 32704, 32831, 32768, 32895),
            (5114, 32704, 32831, 32768, 32895),
            (5115, 32704, 32831, 32768, 32895),
            (5116, 32704, 32831, 32768, 32895),
            (5117, 32704, 32831, 32768, 32895),
            (5118, 32704, 32831, 32768, 32895),
            (5119, 32704, 32831, 32768, 32895),
            (5120, 32704, 32831, 32768, 32895),
            (5121, 32704, 32831, 32768, 32895),
            (5122, 32704, 32831, 32768, 32895),
            (5123, 32704, 32831, 32768, 32895),
            (5124, 32768, 32831, 32768, 32831),
            (5125, 32768, 32831, 32832, 32895),
            (5131, 32768, 32831, 32832, 32895),
            (5132, 32768, 32831, 32832, 32895),
            (5133, 32768, 32831, 32832, 32895),
            (5134, 32768, 32831, 32832, 32895),
            (5140, 32704, 32895, 32768, 32895),
            (5701, 32576, 33023, 32512, 32959),
            (5801, 32512, 32831, 32704, 33023),
            (5802, 32512, 32831, 32704, 33023),
            (5803, 32512, 32831, 32704, 33023),
            (5804, 32512, 32831, 32704, 33023),
            (5805, 32512, 32831, 32704, 33023),
            (7000, 32640, 32959, 32576, 32895),
            (7001, 32640, 32831, 32704, 32895),
            (7002, 32512, 32767, 32512, 32767),
            (7003, 32512, 32767, 32512, 32767),
            (7004, 32512, 32767, 32512, 32767),
            (7005, 32512, 32767, 32512, 32767),
            (7006, 32512, 32767, 32512, 32767),
            (7007, 32704, 32895, 32768, 32959),
            (7008, 32704, 32895, 32768, 32959),
            (7009, 32704, 32895, 32768, 32959),
            (7010, 32704, 32895, 32768, 32959),
            (7011, 32704, 32895, 32768, 32959),
            (7051, 32640, 32959, 32576, 32895),
            (7052, 32640, 32959, 32576, 32895),
            (7053, 32640, 32959, 32576, 32895),
            (7054, 32640, 32959, 32576, 32895),
            (7055, 32640, 32959, 32576, 32895),
            (8011, 32768, 32895, 32768, 32895),
            (8012, 32704, 32895, 32704, 32895),
            (8013, 32704, 32767, 32768, 32831),
            (8014, 32704, 32767, 32704, 32831),
            (8015, 32704, 32831, 32704, 32831),
            (16384, 32704, 32767, 32768, 32831),
            (16896, 32704, 32767, 32768, 32831),
            (17408, 32704, 32767, 32768, 32831),
            (17920, 32704, 32767, 32768, 32831),
            (18432, 32704, 32767, 32768, 32831),
            (18944, 32704, 32767, 32768, 32831),
            (19456, 32704, 32767, 32768, 32831),
            (19968, 32704, 32767, 32768, 32831),
            (20480, 32704, 32767, 32768, 32831),
            (20992, 32704, 32767, 32768, 32831),
            (21504, 32704, 32767, 32768, 32831),
            (22016, 32704, 32767, 32768, 32831),
            (22528, 32704, 32767, 32768, 32831),
            (23040, 32704, 32767, 32768, 32831),
            (23552, 32704, 32767, 32768, 32831),
            (24064, 32704, 32767, 32768, 32831),
            (24576, 32704, 32767, 32768, 32831),
            (25088, 32704, 32767, 32768, 32831))

MAP_DIR = 'maps/'
MAPINFO_MAP_NO = 0
MAPINFO_START_X = 1
MAPINFO_END_X = 2
MAPINFO_START_Y = 3
MAPINFO_END_Y = 4

class TextMapReader():
    def read(self, id = None):
        logging.debug('read map...')
        if not id:
            _maps = {}
            for info in MAP_INFO:
                mapId = info[MAPINFO_MAP_NO]
                xSize = info[MAPINFO_END_X] - info[MAPINFO_START_X] + 1
                ySize = info[MAPINFO_END_Y] - info[MAPINFO_START_Y] + 1
                try:
                    _maps[mapId] = V1Map(mapId,
                                         self._read(mapId, xSize, ySize),
                                         info[MAPINFO_START_X],
                                         info[MAPINFO_START_Y],
                                         MapsTable()._maps[mapId].isUnderwater,
                                         MapsTable()._maps[mapId].isMarkable,
                                         MapsTable()._maps[mapId].isTeleportable,
                                         MapsTable()._maps[mapId].isEscapable,
                                         MapsTable()._maps[mapId].isUseResurrection,
                                         MapsTable()._maps[mapId].isUsePainwand,
                                         MapsTable()._maps[mapId].isEnabledDeathPenalty,
                                         MapsTable()._maps[mapId].isTakePets,
                                         MapsTable()._maps[mapId].isRecallPets,
                                         MapsTable()._maps[mapId].isUsableItem,
                                         MapsTable()._maps[mapId].isUsableSkill)
                except Exception as e:
                    logging.debug('reading map failed...')
                    logging.error(e)
            return _maps
        else:
            for info in MAP_INFO:
                mapId = info[MAPINFO_MAP_NO]
                xSize = info[MAPINFO_END_X] - info[MAPINFO_START_X] + 1
                ySize = info[MAPINFO_END_Y] - info[MAPINFO_START_Y] + 1
                if mapId == id:
                    return V1Map(mapId,
                                 self._read(mapId, xSize, ySize),
                                 info[MAPINFO_START_X],
                                 info[MAPINFO_START_Y],
                                 MapsTable()._maps[mapId].isUnderwater,
                                 MapsTable()._maps[mapId].isMarkable,
                                 MapsTable()._maps[mapId].isTeleportable,
                                 MapsTable()._maps[mapId].isEscapable,
                                 MapsTable()._maps[mapId].isUseResurrection,
                                 MapsTable()._maps[mapId].isUsePainwand,
                                 MapsTable()._maps[mapId].isEnabledDeathPenalty,
                                 MapsTable()._maps[mapId].isTakePets,
                                 MapsTable()._maps[mapId].isRecallPets,
                                 MapsTable()._maps[mapId].isUsableItem,
                                 MapsTable()._maps[mapId].isUsableSkill)
            raise Exception("MapId: " + id)

    def _read(self, mapId, xSize, ySize):
        _map = []
        for line in open(MAP_DIR + str(mapId) + '.txt', 'U'):
            line = line[:-1]
            if len(line) == 0 or line.startswith('#'):
                continue
            _map.append(line.split(','))
        return _map