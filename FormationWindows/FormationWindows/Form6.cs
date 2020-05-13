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
    public partial class Form6 : Form { 
    
        int nb = new Random().Next(1, 100);
        int nbStep = 0;

        public Form6()
        {
            InitializeComponent();
        }

        private void Form6_Load(object sender, EventArgs e)
        {
            // Vous allez générer aléatoirement un nombre entier entre 1 et 1000
            // Vous allez essayer de le deviner
            // Saisir un nombre
            // Cliquer sur un bouton
            // Le programme trop haut ou trop bas ou vous avez gagné
            // Afficher le nombre de coup total
            // Limiter le nombre de coup total, par exemple 10 coups
            // Facultatif : Afficher une picturebox quand vous gagnez et une autre quand vous perdez, .visible=true false
        }

        private void button1_Click(object sender, EventArgs e)
        {
            label4.Text = nb.ToString();
            nbStep += 1;
            if (nbStep > 10)
            {
                label2.Text = "Trop de coups : perdu";
                pictureBox2.Visible = true;
                nb = new Random().Next(1, 1000);
                nbStep = 0;
            }
            else
            {
                textBox2.Text = nbStep.ToString();
                int i = Convert.ToInt32(textBox1.Text);
                if (i > nb)
                {
                    label2.Text = "Trop Haut";
                }
                else if (i < nb)
                {
                    label2.Text = "Trop bas";
                }
                else
                {
                    label2.Text = "Gagné";
                    pictureBox1.Visible = true;
                }
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            nb = new Random().Next(1, 100);
            nbStep = 0;
            label2.Text = "Reset";
            pictureBox1.Visible = false;
            pictureBox2.Visible = false;
        }
    }
}
