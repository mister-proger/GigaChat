﻿using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace GigaChat
{
    public partial class winRegister : Form
    {
        public winRegister()
        {
            InitializeComponent();
        }

        private void exitReg_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void exitReg_MouseHover(object sender, EventArgs e)
        {
            exitReg.BackColor = Color.FromArgb(63,72,204);
        }

        private void exitReg_MouseLeave(object sender, EventArgs e)
        {
            exitReg.BackColor = Color.FromArgb(0, 162, 232); 
        }

        private void registerReg_Click(object sender, EventArgs e)
        {
            this.Hide();
        }

        private void registerReg_MouseHover(object sender, EventArgs e)
        {
            registerReg.Font = new Font("Comic Sans MS",8,FontStyle.Underline);
        }

        private void registerReg_MouseLeave(object sender, EventArgs e)
        {
            registerReg.Font = new Font("Comic Sans MS",8);
        }

        private void passwordVisCheckBox_MouseHover(object sender, EventArgs e)
        {
            passwordVisCheckBox.Font = new Font("Comic Sans MS", 8, FontStyle.Underline);
        }

        private void passwordVisCheckBox_MouseLeave(object sender, EventArgs e)
        {
            passwordVisCheckBox.Font = new Font("Comic Sans MS", 8);
        }

        private void passwordVisCheckBox_Click(object sender, EventArgs e)
        {
            passwordBoxReg.UseSystemPasswordChar = (!passwordBoxReg.UseSystemPasswordChar) ? true : false;
        }

        Point lastPoint;
        private void winRegister_MouseMove(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left)
            {
                this.Left += e.X - lastPoint.X;
                this.Top += e.Y - lastPoint.Y;
            }
        }
        private void winRegister_MouseDown(object sender, MouseEventArgs e)
        {
            lastPoint = new Point(e.X,e.Y);
        }
    }
}
