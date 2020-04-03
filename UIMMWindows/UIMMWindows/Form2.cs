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
    public partial class Form2 : Form
    {
        public Form2()
        {
            InitializeComponent();
        }

        private void Form2_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            string s = textBox1.Text;
            int n = Convert.ToInt32(s);
            bool b = isPrime(n);
            if(b == true)
            {
                textBox2.Text = s + " est premier";
            }
            else
            {
                textBox2.Text = s + " n'est pas premier";
            }
        }

        private bool isPrime(int n)
        {
            if(n<2)
            {
                return false;
            }
            else
            {
                for(int i=2;i<n;i++)
                {
                    if(n % i == 0) {
                        return false;
                    }
                }
                return true;
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            panel1.Visible = true;
            
        }

        private void button3_Click(object sender, EventArgs e)
        {
            string pwd = textBox3.Text;
            if (pwd == "toto")
            {
                Form1 f1 = new Form1();
                this.Visible = false;
                f1.Show();
            }
        }
    }
}
