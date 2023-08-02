package com.ZSTeam.gigachat

import android.content.Context
import android.widget.TextView
import io.ktor.client.HttpClient
import io.ktor.client.request.forms.submitForm
import io.ktor.client.statement.bodyAsText
import io.ktor.client.statement.readText
import io.ktor.http.Parameters

class User(context: Context) {
    private val httpClient = HttpClient()
    lateinit var token: String
    var connected = false

//    init {
//        context.getSharedPreferences("user", Context.MODE_PRIVATE).apply {
//            token = getString("token", "").toString()
//            if (token.isNotEmpty()) {
//                connected = true
//            }
//        }
//    }

    suspend fun sendMessage(message: String, callbackWidget: TextView, messageResponse: Int = 0) {
        val response = httpClient.submitForm(
            url = "http://192.168.28.56:8001/",
            formParameters = Parameters.build {
                append("message", message)
            }
        )
        callbackWidget.text = response.bodyAsText()
    }
}