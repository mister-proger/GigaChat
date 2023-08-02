package com.ZSTeam.gigachat

import android.os.Bundle
import android.widget.Button
import android.widget.EditText
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity
import kotlinx.coroutines.runBlocking

class Loader : AppCompatActivity() {
    val client = User(this)

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_loader)

        widgetSettings()
    }

    private fun widgetSettings() {
        val sendButton = findViewById<Button>(R.id.sendButton)
        val inputText = findViewById<EditText>(R.id.inputText)
        val viewText = findViewById<TextView>(R.id.viewText)
        sendButton.setOnClickListener {
            runBlocking {
                client.sendMessage(inputText.text.toString(), viewText)
            }
        }
    }
}