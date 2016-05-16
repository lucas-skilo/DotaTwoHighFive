using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Text;
using System.Threading.Tasks;

using Dota_Two_High_Five.Command_Types;
using Dota_Two_High_Five.Command_Types.GetMatchHistoryBySequenceNum;
using Newtonsoft.Json;

namespace Dota_Two_High_Five.Web_and_JSON
{
    public class MatchGetter
    {
        string GetWebpageURL(string command, params string[] arguments)
        {
            string key = "key=2179FDF11489B59187A1AD12B4B1E2C9";
            string url = "https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/V001/?";

            foreach (string arg in arguments)
            {
                url = url + arg + "&";
            }
            url = url + key;

            return url;
        }

        string ReadJsonFromURL(string url)
        {
            WebClient wc = new WebClient();
            byte[] pageContent = wc.DownloadData(url);
            return System.Text.Encoding.UTF8.GetString(pageContent);
        }

        public IList<MatchDetails> GetMatchesStartingOnSeqNumber(UInt64 seqNumber)
        {
            IList<MatchDetails> matchList;
            MatchHistoryBySequenceNum matchHistory;
            string url;
            string json;

            url = GetWebpageURL("GetMatchHistoryBySequenceNum", "start_at_match_seq_num=" + seqNumber);
            json = ReadJsonFromURL(url);

            matchHistory = JsonConvert.DeserializeObject<MatchHistoryBySequenceNum>(json);
            matchList = matchHistory.result.matches;

            return matchList;
        }
    }
}
