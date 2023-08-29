package com.example.demoapi.controllers

import org.slf4j.LoggerFactory
import com.example.demoapi.services.HelloService
import com.example.demoapi.interceptors.CorrelationInterceptor
import org.springframework.web.bind.annotation.GetMapping
import org.springframework.web.bind.annotation.RequestMapping
import org.springframework.web.bind.annotation.RestController

@RestController
@RequestMapping("/api")
class HelloWorldController (private val helloService: HelloService) {

    private val logger = LoggerFactory.getLogger(HelloWorldController::class.java)
    @GetMapping("/hello")
    fun sayHello(): String {
        logger.info("sayHello endpoint was called!")
        val correlationId = CorrelationInterceptor.getCorrelationId()
        return "${helloService.getHelloMessage()} (Correlation ID: $correlationId)"
    }   
}
