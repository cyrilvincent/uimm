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
        }

        private void Form3_Load(object sender, EventArgs e)
        {

        }
    }
}
