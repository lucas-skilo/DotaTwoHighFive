﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Dota_Two_High_Five.Command_Types
{
    public class MatchDetails
    {
        public IList<Player> players { get; set; }
        public bool radiant_win { get; set; }
        public Int16 duration { get; set; }
        public UInt64 start_time { get; set; }
        public UInt64 match_id { get; set; }
        public UInt64 match_seq_num { get; set; }
        public UInt16 tower_status_radiant { get; set; }
        public UInt16 tower_status_dire { get; set; }
        public Byte barracks_status_radiant { get; set; }
        public Byte barracks_status_dire { get; set; }
        public Int16 first_blood_time { get; set; }
        public Byte lobby_type { get; set; }
        public Byte human_players { get; set; }
        public Byte game_mode { get; set; }
        public Int16 radiant_score { get; set; }
        public Int16 dire_score { get; set; }
    }
}
