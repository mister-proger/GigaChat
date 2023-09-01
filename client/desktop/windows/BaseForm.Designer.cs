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
            this.centeralWidget = new System.Windows.Forms.Panel();
            this.centralWidget = new System.Windows.Forms.Panel();
            this.downLayoutPanel = new System.Windows.Forms.Panel();
            this.CenterLayout = new System.Windows.Forms.Panel();
            this.SuspendLayout();
            // 
            // chatsIconsLayout
            // 
            this.chatsIconsLayout.AccessibleRole = System.Windows.Forms.AccessibleRole.ScrollBar;
            this.chatsIconsLayout.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left)));
            this.chatsIconsLayout.AutoScroll = true;
            this.chatsIconsLayout.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(20)))), ((int)(((byte)(20)))), ((int)(((byte)(20)))));
            this.chatsIconsLayout.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.chatsIconsLayout.Cursor = System.Windows.Forms.Cursors.Default;
            this.chatsIconsLayout.Enabled = false;
            this.chatsIconsLayout.Location = new System.Drawing.Point(-6, -1);
            this.chatsIconsLayout.Name = "chatsIconsLayout";
            this.chatsIconsLayout.Size = new System.Drawing.Size(78, 489);
            this.chatsIconsLayout.TabIndex = 0;
            // 
            // centeralWidget
            // 
            this.centeralWidget.AutoScroll = true;
            this.centeralWidget.AutoScrollMinSize = new System.Drawing.Size(729, 399);
            this.centeralWidget.AutoSize = true;
            this.centeralWidget.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(50)))), ((int)(((byte)(50)))), ((int)(((byte)(50)))));
            this.centeralWidget.Cursor = System.Windows.Forms.Cursors.Default;
            this.centeralWidget.Dock = System.Windows.Forms.DockStyle.Right;
            this.centeralWidget.Location = new System.Drawing.Point(816, 0);
            this.centeralWidget.Name = "centeralWidget";
            this.centeralWidget.Size = new System.Drawing.Size(0, 489);
            this.centeralWidget.TabIndex = 3;
            // 
            // centralWidget
            // 
            this.centralWidget.AutoSize = true;
            this.centralWidget.Dock = System.Windows.Forms.DockStyle.Right;
            this.centralWidget.Location = new System.Drawing.Point(816, 0);
            this.centralWidget.Name = "centralWidget";
            this.centralWidget.Size = new System.Drawing.Size(0, 489);
            this.centralWidget.TabIndex = 4;
            // 
            // downLayoutPanel
            // 
            this.downLayoutPanel.AccessibleRole = System.Windows.Forms.AccessibleRole.ScrollBar;
            this.downLayoutPanel.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.downLayoutPanel.AutoScroll = true;
            this.downLayoutPanel.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(30)))), ((int)(((byte)(30)))), ((int)(((byte)(30)))));
            this.downLayoutPanel.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.downLayoutPanel.Cursor = System.Windows.Forms.Cursors.Default;
            this.downLayoutPanel.Enabled = false;
            this.downLayoutPanel.Location = new System.Drawing.Point(69, 424);
            this.downLayoutPanel.Name = "downLayoutPanel";
            this.downLayoutPanel.Size = new System.Drawing.Size(747, 64);
            this.downLayoutPanel.TabIndex = 1;
            // 
            // CenterLayout
            // 
            this.CenterLayout.AccessibleRole = System.Windows.Forms.AccessibleRole.ScrollBar;
            this.CenterLayout.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.CenterLayout.AutoScroll = true;
            this.CenterLayout.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(50)))), ((int)(((byte)(50)))), ((int)(((byte)(50)))));
            this.CenterLayout.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.CenterLayout.Cursor = System.Windows.Forms.Cursors.Default;
            this.CenterLayout.Enabled = false;
            this.CenterLayout.Location = new System.Drawing.Point(69, -1);
            this.CenterLayout.Name = "CenterLayout";
            this.CenterLayout.Size = new System.Drawing.Size(747, 425);
            this.CenterLayout.TabIndex = 2;
            // 
            // BaseForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(40)))), ((int)(((byte)(40)))), ((int)(((byte)(40)))));
            this.ClientSize = new System.Drawing.Size(816, 489);
            this.Controls.Add(this.chatsIconsLayout);
            this.Controls.Add(this.downLayoutPanel);
            this.Controls.Add(this.centralWidget);
            this.Controls.Add(this.centeralWidget);
            this.Controls.Add(this.CenterLayout);
            this.Cursor = System.Windows.Forms.Cursors.Default;
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.MinimumSize = new System.Drawing.Size(816, 489);
            this.Name = "BaseForm";
            this.Text = "GigaChat";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Panel chatsIconsLayout;
        private System.Windows.Forms.Panel centeralWidget;
        private System.Windows.Forms.Panel centralWidget;
        private System.Windows.Forms.Panel downLayoutPanel;
        private System.Windows.Forms.Panel CenterLayout;
    }
}