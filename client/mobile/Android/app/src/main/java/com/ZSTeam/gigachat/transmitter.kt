package com.zsteam.gigachat

import android.content.Context
import io.ktor.client.HttpClient
import io.ktor.client.plugins.websocket.webSocketSession
import io.ktor.client.request.forms.submitForm
import io.ktor.client.statement.HttpResponse
import io.ktor.client.statement.bodyAsText
import io.ktor.http.Parameters

class User(context: Context) {
    private val httpClient = HttpClient()
    private lateinit var token: String
    private lateinit var socket: Any
    var connected = false
    private val prefs = context.getSharedPreferences("authentication", Context.MODE_PRIVATE)

    init {
        val ttoken = prefs.getString("token", "")!!
        if (ttoken.isNotEmpty()) {
            token = ttoken
        }
    }

    suspend fun auth(login: String, password: String): Boolean {
        val response: HttpResponse
        try {
            response = httpClient.submitForm(
                url = "http://192.168.0.15:8001/",
                formParameters = Parameters.build {
                    append("login", login)
                    append("password", password)
                }
            )
        } catch (e: Exception) {
            return false
        }
        return if (response.bodyAsText().isNotEmpty()) {
            token = response.bodyAsText()
            true
        } else {
            false
        }
    }

    suspend fun connect(): Boolean {
        return try {
            val response = httpClient.submitForm(
                url = "http://192.168.0.15:8001/authenticate/?token=$token"
            )
            socket = httpClient.webSocketSession {
                endpoint = "ws://192.168.0.15:8002/connection/message"
            }
            true
        } catch (e: Exception) {
            false
        }
    }

    suspend fun disconnect(): Boolean {
         TODO("Not yet implemented")
    }
}
