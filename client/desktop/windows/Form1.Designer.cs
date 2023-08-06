using System;

namespace GigaChat
{
    partial class winRegister
    {
        /// <summary>
        /// Обязательная переменная конструктора.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Освободить все используемые ресурсы.
        /// </summary>
        /// <param name="disposing">истинно, если управляемый ресурс должен быть удален; иначе ложно.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Код, автоматически созданный конструктором форм Windows

        /// <summary>
        /// Требуемый метод для поддержки конструктора — не изменяйте 
        /// содержимое этого метода с помощью редактора кода.
        /// </summary>
        private void InitializeComponent()
        {
            this.exitReg = new System.Windows.Forms.Label();
            this.WelcomeBackReg = new System.Windows.Forms.Label();
            this.LogInLabelReg = new System.Windows.Forms.Label();
            this.loginBoxReg = new System.Windows.Forms.TextBox();
            this.loginReg = new System.Windows.Forms.Label();
            this.passwordReg = new System.Windows.Forms.Label();
            this.passwordBoxReg = new System.Windows.Forms.TextBox();
            this.LOGINbuttonReg = new System.Windows.Forms.Button();
            this.passwordVisCheckBox = new System.Windows.Forms.CheckBox();
            this.registerReg = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // exitReg
            // 
            this.exitReg.AutoSize = true;
            this.exitReg.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(0)))), ((int)(((byte)(162)))), ((int)(((byte)(232)))));
            this.exitReg.Cursor = System.Windows.Forms.Cursors.Hand;
            this.exitReg.Font = new System.Drawing.Font("Comic Sans MS", 14F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.exitReg.ForeColor = System.Drawing.Color.Black;
            this.exitReg.Location = new System.Drawing.Point(762, -2);
            this.exitReg.Name = "exitReg";
            this.exitReg.Size = new System.Drawing.Size(23, 27);
            this.exitReg.TabIndex = 0;
            this.exitReg.Text = "x";
            this.exitReg.TextAlign = System.Drawing.ContentAlignment.TopRight;
            this.exitReg.UseMnemonic = false;
            this.exitReg.Click += new System.EventHandler(this.exitReg_Click);
            this.exitReg.MouseLeave += new System.EventHandler(this.exitReg_MouseLeave);
            this.exitReg.MouseHover += new System.EventHandler(this.exitReg_MouseHover);
            // 
            // WelcomeBackReg
            // 
            this.WelcomeBackReg.AutoSize = true;
            this.WelcomeBackReg.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(58)))), ((int)(((byte)(105)))), ((int)(((byte)(243)))));
            this.WelcomeBackReg.Font = new System.Drawing.Font("Comic Sans MS", 24F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.WelcomeBackReg.ForeColor = System.Drawing.Color.White;
            this.WelcomeBackReg.Location = new System.Drawing.Point(34, 31);
            this.WelcomeBackReg.Name = "WelcomeBackReg";
            this.WelcomeBackReg.Size = new System.Drawing.Size(335, 45);
            this.WelcomeBackReg.TabIndex = 1;
            this.WelcomeBackReg.Text = "С ВОЗВРАЩЕНИЕМ!";
            // 
            // LogInLabelReg
            // 
            this.LogInLabelReg.AutoSize = true;
            this.LogInLabelReg.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(58)))), ((int)(((byte)(105)))), ((int)(((byte)(243)))));
            this.LogInLabelReg.Font = new System.Drawing.Font("Comic Sans MS", 26F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.LogInLabelReg.ForeColor = System.Drawing.Color.White;
            this.LogInLabelReg.Location = new System.Drawing.Point(337, 162);
            this.LogInLabelReg.Name = "LogInLabelReg";
            this.LogInLabelReg.Size = new System.Drawing.Size(124, 49);
            this.LogInLabelReg.TabIndex = 2;
            this.LogInLabelReg.Text = "ВХОД";
            // 
            // loginBoxReg
            // 
            this.loginBoxReg.Font = new System.Drawing.Font("Comic Sans MS", 12F, ((System.Drawing.FontStyle)((System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic))), System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.loginBoxReg.Location = new System.Drawing.Point(323, 227);
            this.loginBoxReg.MaxLength = 16;
            this.loginBoxReg.Name = "loginBoxReg";
            this.loginBoxReg.Size = new System.Drawing.Size(155, 30);
            this.loginBoxReg.TabIndex = 3;
            // 
            // loginReg
            // 
            this.loginReg.AutoSize = true;
            this.loginReg.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(58)))), ((int)(((byte)(105)))), ((int)(((byte)(243)))));
            this.loginReg.Font = new System.Drawing.Font("Comic Sans MS", 16F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.loginReg.ForeColor = System.Drawing.Color.White;
            this.loginReg.Location = new System.Drawing.Point(229, 227);
            this.loginReg.Name = "loginReg";
            this.loginReg.Size = new System.Drawing.Size(77, 31);
            this.loginReg.TabIndex = 4;
            this.loginReg.Text = "логин";
            // 
            // passwordReg
            // 
            this.passwordReg.AutoSize = true;
            this.passwordReg.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(58)))), ((int)(((byte)(105)))), ((int)(((byte)(243)))));
            this.passwordReg.Font = new System.Drawing.Font("Comic Sans MS", 16F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.passwordReg.ForeColor = System.Drawing.Color.White;
            this.passwordReg.Location = new System.Drawing.Point(229, 278);
            this.passwordReg.Name = "passwordReg";
            this.passwordReg.Size = new System.Drawing.Size(90, 31);
            this.passwordReg.TabIndex = 6;
            this.passwordReg.Text = "пароль";
            // 
            // passwordBoxReg
            // 
            this.passwordBoxReg.Font = new System.Drawing.Font("Comic Sans MS", 12F, ((System.Drawing.FontStyle)((System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic))), System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.passwordBoxReg.Location = new System.Drawing.Point(323, 278);
            this.passwordBoxReg.MaxLength = 32;
            this.passwordBoxReg.Name = "passwordBoxReg";
            this.passwordBoxReg.Size = new System.Drawing.Size(155, 30);
            this.passwordBoxReg.TabIndex = 5;
            this.passwordBoxReg.UseSystemPasswordChar = true;
            // 
            // LOGINbuttonReg
            // 
            this.LOGINbuttonReg.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(58)))), ((int)(((byte)(105)))), ((int)(((byte)(243)))));
            this.LOGINbuttonReg.BackgroundImage = global::GigaChat.Properties.Resources.loginBN;
            this.LOGINbuttonReg.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Center;
            this.LOGINbuttonReg.Cursor = System.Windows.Forms.Cursors.Hand;
            this.LOGINbuttonReg.Font = new System.Drawing.Font("Comic Sans MS", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.LOGINbuttonReg.Location = new System.Drawing.Point(346, 325);
            this.LOGINbuttonReg.Name = "LOGINbuttonReg";
            this.LOGINbuttonReg.Size = new System.Drawing.Size(115, 35);
            this.LOGINbuttonReg.TabIndex = 7;
            this.LOGINbuttonReg.Text = "войти";
            this.LOGINbuttonReg.UseVisualStyleBackColor = false;
            // 
            // passwordVisCheckBox
            // 
            this.passwordVisCheckBox.AutoSize = true;
            this.passwordVisCheckBox.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(58)))), ((int)(((byte)(105)))), ((int)(((byte)(243)))));
            this.passwordVisCheckBox.Font = new System.Drawing.Font("Comic Sans MS", 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.passwordVisCheckBox.Location = new System.Drawing.Point(484, 287);
            this.passwordVisCheckBox.Name = "passwordVisCheckBox";
            this.passwordVisCheckBox.Size = new System.Drawing.Size(115, 20);
            this.passwordVisCheckBox.TabIndex = 8;
            this.passwordVisCheckBox.Text = "показать пароль";
            this.passwordVisCheckBox.UseVisualStyleBackColor = false;
            this.passwordVisCheckBox.Click += new System.EventHandler(this.passwordVisCheckBox_Click);
            // 
            // registerReg
            // 
            this.registerReg.AutoSize = true;
            this.registerReg.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(58)))), ((int)(((byte)(105)))), ((int)(((byte)(243)))));
            this.registerReg.Font = new System.Drawing.Font("Comic Sans MS", 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.registerReg.Location = new System.Drawing.Point(355, 363);
            this.registerReg.Name = "registerReg";
            this.registerReg.Size = new System.Drawing.Size(106, 16);
            this.registerReg.TabIndex = 9;
            this.registerReg.Text = "еще нет аккаунта?";
            this.registerReg.Click += new System.EventHandler(this.registerReg_Click);
            // 
            // winRegister
            // 
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.None;
            this.BackgroundImage = global::GigaChat.Properties.Resources.RegisterBG;
            this.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Center;
            this.ClientSize = new System.Drawing.Size(784, 500);
            this.Controls.Add(this.registerReg);
            this.Controls.Add(this.passwordVisCheckBox);
            this.Controls.Add(this.LOGINbuttonReg);
            this.Controls.Add(this.passwordReg);
            this.Controls.Add(this.passwordBoxReg);
            this.Controls.Add(this.loginReg);
            this.Controls.Add(this.loginBoxReg);
            this.Controls.Add(this.LogInLabelReg);
            this.Controls.Add(this.WelcomeBackReg);
            this.Controls.Add(this.exitReg);
            this.ForeColor = System.Drawing.Color.White;
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.None;
            this.Name = "winRegister";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "GigaChat --Register";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion
        private System.Windows.Forms.Label exitReg;
        private System.Windows.Forms.Label WelcomeBackReg;
        private System.Windows.Forms.Label LogInLabelReg;
        private System.Windows.Forms.TextBox loginBoxReg;
        private System.Windows.Forms.Label loginReg;
        private System.Windows.Forms.Label passwordReg;
        private System.Windows.Forms.TextBox passwordBoxReg;
        private System.Windows.Forms.Button LOGINbuttonReg;
        private System.Windows.Forms.CheckBox passwordVisCheckBox;
        private System.Windows.Forms.Label registerReg;
    }
}

