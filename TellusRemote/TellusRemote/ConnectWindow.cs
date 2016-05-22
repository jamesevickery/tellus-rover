using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Net;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace TellusRemote
{
    public partial class ConnectWindow : Form
    {
        public ConnectWindow()
        {
            InitializeComponent();
        }

        private void buttConnect_Click(object sender, EventArgs e)
        {
            string errorCode = ErrorText(textIP.Text, textCP.Text, textVP.Text);
            if(errorCode != null)
            {// Invalid input
                MessageBox.Show(errorCode,
                    "Tellus: Input Error",
                    MessageBoxButtons.OK,
                    MessageBoxIcon.Error);
            }
            else
            {// Input all valid

            }
        }

        private string ErrorText(string testIP, string testCP, string testVP)
        {
            if (!IsValidIP(testIP)) return ("Invalid IP: " + testIP);
            if (!IsValidPort(testCP)) return ("Invalid port: " + testCP);
            if (!IsValidPort(testVP)) return ("Invalid port: " + testVP);
            return null;
        }

        private bool IsValidIP(string testIP)
        {
            IPAddress validatedIP;
            return IPAddress.TryParse(testIP, out validatedIP);
        }

        private bool IsValidPort(string testPort)
        {
            int portNum;
            if (int.TryParse(testPort, out portNum)
                && portNum >= 0
                && portNum <= 65535) return true;
            else return false;
        }

        private void buttSetD_Click(object sender, EventArgs e)
        {

        }

        private void buttLoadD_Click(object sender, EventArgs e)
        {

        }
    }
}
