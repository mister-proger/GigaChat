namespace GigaChat
{
    partial class BaseForm
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(BaseForm));
            this.chatsIconsLayout = new System.Windows.Forms.Panel();
            this.horizontalLayout = new System.Windows.Forms.Panel();
            this.panel1 = new System.Windows.Forms.Panel();
            this.SuspendLayout();
            // 
            // chatsIconsLayout
            // 
            this.chatsIconsLayout.Anchor = System.Windows.Forms.AnchorStyles.Left;
            this.chatsIconsLayout.AutoSize = true;
            this.chatsIconsLayout.Cursor = System.Windows.Forms.Cursors.Default;
            this.chatsIconsLayout.Location = new System.Drawing.Point(1, 0);
            this.chatsIconsLayout.Name = "chatsIconsLayout";
            this.chatsIconsLayout.Size = new System.Drawing.Size(70, 461);
            this.chatsIconsLayout.TabIndex = 0;
            // 
            // horizontalLayout
            // 
            this.horizontalLayout.Anchor = System.Windows.Forms.AnchorStyles.Left;
            this.horizontalLayout.AutoSize = true;
            this.horizontalLayout.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(40)))), ((int)(((byte)(40)))), ((int)(((byte)(40)))));
            this.horizontalLayout.Cursor = System.Windows.Forms.Cursors.Default;
            this.horizontalLayout.Location = new System.Drawing.Point(70, 398);
            this.horizontalLayout.Name = "horizontalLayout";
            this.horizontalLayout.Size = new System.Drawing.Size(729, 50);
            this.horizontalLayout.TabIndex = 2;
            // 
            // panel1
            // 
            this.panel1.Anchor = System.Windows.Forms.AnchorStyles.Left;
            this.panel1.AutoSize = true;
            this.panel1.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(50)))), ((int)(((byte)(50)))), ((int)(((byte)(50)))));
            this.panel1.Cursor = System.Windows.Forms.Cursors.Default;
            this.panel1.Location = new System.Drawing.Point(70, 0);
            this.panel1.Name = "panel1";
            this.panel1.Size = new System.Drawing.Size(729, 399);
            this.panel1.TabIndex = 3;
            // 
            // BaseForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.AutoScroll = true;
            this.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(40)))), ((int)(((byte)(40)))), ((int)(((byte)(40)))));
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.panel1);
            this.Controls.Add(this.horizontalLayout);
            this.Controls.Add(this.chatsIconsLayout);
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.Name = "BaseForm";
            this.Text = "BaseForm";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Panel chatsIconsLayout;
        private System.Windows.Forms.Panel horizontalLayout;
        private System.Windows.Forms.Panel panel1;
    }
}