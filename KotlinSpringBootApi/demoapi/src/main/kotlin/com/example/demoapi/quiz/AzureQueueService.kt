package com.example.demoapi.quiz

import com.azure.storage.queue.QueueClientBuilder
import com.example.demoapi.services.CorrelationIdService
import com.fasterxml.jackson.databind.ObjectMapper
import org.slf4j.LoggerFactory
import org.springframework.beans.factory.annotation.Value
import org.springframework.stereotype.Service

@Service
class AzureQueueService(private val objectMapper: ObjectMapper, private val correlationIdService: CorrelationIdService, mapper: ObjectMapper){

    private val logger = LoggerFactory.getLogger(this::class.java)

    fun sendQuizMessage(quizRequest: QuizRequest) {
        logger.info("Sending quiz response to the queue!")
        val messageObj = QueueMessage(quizRequest, correlationIdService.getCorrelationId() ?: "")
        val messagePayload = objectMapper.writeValueAsString(messageObj)

        this.sendMessage("QuizQueue", messagePayload)
    }

    @Value("\${azure.storage.connection-string}")
    private lateinit var connectionString: String

    private fun sendMessage(queueName: String, message: String) {

        val client = QueueClientBuilder()
                .connectionString(connectionString)
                .queueName(queueName)
                .buildClient()

        client.sendMessage(message)
        logger.info("Message fly away to: $queueName!")
    }
}
