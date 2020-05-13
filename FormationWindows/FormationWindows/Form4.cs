using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace FormationWindows
{
    public partial class Form4 : Form
    {
        public Form4()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int n = Convert.ToInt32(textBox1.Text);
            bool res = isPrime(n);
            if(res == true)
            {
                label1.Text = "C'est un nombre premier";
            }
            else
            {
                label1.Text = "Ce n'est pas un nombre premier";
            }
        }

        bool isPrime(int n)
        {
            if(n < 2)
            {
                return false;
            }
            else
            {
                for(int i = 2; i < n; i++)
                {
                    if(n % i == 0)
                    {
                        return false;
                    }
                }
                return true;
            }
        }
    }
}
