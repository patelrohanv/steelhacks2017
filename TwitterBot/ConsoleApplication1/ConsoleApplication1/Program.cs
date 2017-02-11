using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Net;
using System.IO;
using TweetSharp;

namespace ConsoleApplication1
{
    class Program
    {
        // vars
        static Random ran = new Random();
        static Dictionary<string, Dictionary<string, int>> markovDict = new Dictionary<string, Dictionary<string, int>>();

        static void Main(string[] args)
        {
            /*
            FileStream filestream = new FileStream("out.txt", FileMode.Create);
            var streamWriter = new StreamWriter(filestream);
            streamWriter.AutoFlush = true;
            Console.SetOut(streamWriter);
            Console.SetError(streamWriter);
             */

            PostTweet("testtweet yo");
            Console.WriteLine("End of program. Press any key to exit.");
            Console.ReadKey();
        } // end Main

        static int RandomInt(int min = 1, int max = 5000) // choose random number
        {
            int result = 0;
            result = ran.Next(min, max);
            return result;
        } // end RandomIn


        static void PostTweet(string textToTweet)
        {

            var service = new TwitterService("ZoSd0CJN61VpfgjWVAeIpjjib", "11hd2TiCXz7Fv8zZre7cwD1prXsOmBbB8roVr8Mw1PfZetgwIJ");
            Console.WriteLine("set up new TwitterService");
            service.AuthenticateWith("830431809779466240-YTWx5zkdbnynSAqH1mkajmLl1WfLXJI", "y8UNy0c2WVk1yCiaM6plSDvjorZyUAXOGINehmpoT6ifS");
            Console.WriteLine("authenticated");
            SendTweetOptions tweet = new SendTweetOptions();
            Console.WriteLine("created tweet");
            Console.WriteLine("{0}", textToTweet);
            tweet.Status = textToTweet;
            Console.WriteLine("assigned status to tweet");
            service.SendTweet(tweet);
            Console.WriteLine("tweet sent!");

        } // end PostTweet
    }
}