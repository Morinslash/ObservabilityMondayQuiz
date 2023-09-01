package com.example.demoapi.quiz

import com.fasterxml.jackson.databind.ObjectMapper
import org.slf4j.LoggerFactory
import org.springframework.web.bind.annotation.PostMapping
import org.springframework.web.bind.annotation.RequestBody
import org.springframework.web.bind.annotation.RequestMapping
import org.springframework.web.bind.annotation.RestController

@RestController
@RequestMapping("/api/quiz")
class QuizController( private val azureQueueService: AzureQueueService){
    private val logger = LoggerFactory.getLogger(this::class.java)
    @PostMapping
    fun submitQuiz(@RequestBody quizRequest: QuizRequest): String {
        logger.info("Getting quiz response!")
        azureQueueService.sendQuizMessage(quizRequest)
        return "Check score later!"
    }
}
