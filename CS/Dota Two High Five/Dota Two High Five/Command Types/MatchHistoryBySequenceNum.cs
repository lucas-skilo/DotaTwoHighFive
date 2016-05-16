using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Dota_Two_High_Five.Command_Types.GetMatchHistoryBySequenceNum
{
    public class MatchHistoryBySequenceNum
    {
        public MatchHistoryBySequenceNumResult result { get; set; }
    }

    public class MatchHistoryBySequenceNumResult
    {
        public Byte status { get; set; }
        public string statusDetail { get; set; }
        public IList<MatchDetails> matches { get; set; }
    }
}
