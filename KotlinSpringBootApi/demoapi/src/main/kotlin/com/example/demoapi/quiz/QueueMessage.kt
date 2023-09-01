package com.example.demoapi.quiz

data class QueueMessage<T>(
        val payload: T,
        val correlationId: String
)
