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
    public partial class Form5 : Form
    {
        double abattement = 0.8;
        Random random = new Random();

        public Form5()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            double revenu = Convert.ToDouble(textBox1.Text);
            double nbPart = Convert.ToDouble(textBox2.Text);
            double salaire = (revenu * abattement) / nbPart;
            double res = calcImpots(salaire);
            textBox3.Text = res.ToString();
            double taux = (res * 100) / revenu;
            textBox4.Text = taux.ToString() + "%";
            int aleatoire  = random.Next(0, 1000);
            textBox5.Text = aleatoire.ToString();
        }

        double calcImpots(double salaire)
        {
            if (salaire < 10064)
            {
                return 0;
            }
            else if (salaire < 27794)
            {
                return (salaire - 10064) * 0.14;
            }
            else if (salaire < 74517)
            {
                return (27794 - 10064) * 0.14 + (salaire - 27794) * 0.3;
            }
            else if (salaire < 157806)
            {
                return (27794 - 10064) * 0.14 + (74517 - 27794) * 0.3 + (salaire - 74517) * 0.41;
            }
            else
            {
                return (27794 - 10064) * 0.14 + (74517 - 27794) * 0.3 + (157806 - 74517) * 0.41 + (salaire - 157806) * 0.45;
            }
        }
    }
}
