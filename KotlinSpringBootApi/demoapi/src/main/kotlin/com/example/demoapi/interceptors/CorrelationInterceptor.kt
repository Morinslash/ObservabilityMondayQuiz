package com.example.demoapi.interceptors

import com.example.demoapi.services.CorrelationIdService
import org.slf4j.MDC
import org.springframework.stereotype.Component
import org.springframework.web.servlet.HandlerInterceptor
import org.springframework.beans.factory.annotation.Autowired

@Component
class CorrelationInterceptor(@Autowired private val correlationIdService: CorrelationIdService) : HandlerInterceptor {

    override fun preHandle(request: jakarta.servlet.http.HttpServletRequest, response: jakarta.servlet.http.HttpServletResponse, handler: Any): Boolean {
        val correlationId = request.getHeader("X-Correlation-ID") ?: java.util.UUID.randomUUID().toString()
        correlationIdService.setCorrelationId(correlationId)
        return true
    }

    override fun afterCompletion(request: jakarta.servlet.http.HttpServletRequest, response: jakarta.servlet.http.HttpServletResponse, handler: Any, ex: Exception?) {
        correlationIdService.clearCorrelationId()
    }

}
