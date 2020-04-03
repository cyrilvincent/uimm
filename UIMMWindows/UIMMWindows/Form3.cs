using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace UIMMWindows
{
    public partial class Form3 : Form
    {
        int nb = new Random().Next(1, 100);
        int nbTry = 0;

        public Form3()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string s = textBox1.Text;
            int i = Convert.ToInt32(s);
            if(i == nb)
            {
                label1.Text = "You WIN";
            }
            else if(i > nb)
            {
                label1.Text = "To High";
            }
            else
            {
                label1.Text = "To Low";
            }
            nbTry += 1;
            label2.Text = "Vous avez effectué " + nbTry + " coup(s)";
        }

        private void Form3_Load(object sender, EventArgs e)
        {

        }

        private void button2_Click(object sender, EventArgs e)
        {
            nb = new Random().Next(1, 100);
            nbTry = 0;
            textBox1.Text = "";
            label1.Text = "";
            label2.Text = "";
        }
    }
}
