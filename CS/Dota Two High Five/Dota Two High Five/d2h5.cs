using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using Dota_Two_High_Five.Web_and_JSON;
using Dota_Two_High_Five.Command_Types;

namespace Dota_Two_High_Five
{
    class d2h5
    {
        static void Main(string[] args)
        {
            UInt64 seqNumber = 2071803989;
            IList<MatchDetails> matchList;
            MatchGetter mg = new MatchGetter();

            matchList = mg.GetMatchesStartingOnSeqNumber(seqNumber);

            Console.ReadKey();
        }
    }
}
