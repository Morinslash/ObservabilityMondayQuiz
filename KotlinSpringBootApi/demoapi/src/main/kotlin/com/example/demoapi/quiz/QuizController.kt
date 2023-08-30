package com.example.demoapi.quiz

import com.example.demoapi.controllers.HelloWorldController
import org.slf4j.LoggerFactory
import org.springframework.web.bind.annotation.PostMapping
import org.springframework.web.bind.annotation.RequestBody
import org.springframework.web.bind.annotation.RequestMapping
import org.springframework.web.bind.annotation.RestController

@RestController
@RequestMapping("/api/quiz")
class QuizController {
    private val logger = LoggerFactory.getLogger(this::class.java)
    @PostMapping
    fun submitQuiz(@RequestBody quizRequest: QuizRequest): String {
        // Handle the quiz request here. For now, just return a simple message.
        logger.info("Getting quiz response!")
        return "Received question ${quizRequest.question} with response ${quizRequest.response}"
    }
}
