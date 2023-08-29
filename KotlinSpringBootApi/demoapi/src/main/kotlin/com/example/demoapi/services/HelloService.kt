package com.example.demoapi.services

import org.slf4j.LoggerFactory
import org.springframework.stereotype.Service

@Service
class HelloService {

    private val logger = LoggerFactory.getLogger(HelloService::class.java)
    fun getHelloMessage(): String {
        logger.info("getHelloMessage was called!")
        return "Hello, Kotlin!"
    }
}
