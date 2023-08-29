package com.example.demoapi.interceptors

import org.slf4j.MDC
import org.springframework.lang.Nullable
import org.springframework.stereotype.Component
import org.springframework.web.servlet.HandlerInterceptor

@Component
class CorrelationInterceptor : HandlerInterceptor {
    companion object {
        private val correlationIdThreadLocal = ThreadLocal<String>()

        fun getCorrelationId(): String? = correlationIdThreadLocal.get()
        fun setCorrelationId(correlationId: String) {
            correlationIdThreadLocal.set(correlationId)
        }
    }

    override fun preHandle(request: jakarta.servlet.http.HttpServletRequest, response: jakarta.servlet.http.HttpServletResponse, handler: Any): Boolean {
        val correlationId = request.getHeader("X-CorrelationId") ?: java.util.UUID.randomUUID().toString()
        MDC.put("correlationId", correlationId)
        setCorrelationId(correlationId)
        return true
    }

    override fun afterCompletion(request: jakarta.servlet.http.HttpServletRequest, response: jakarta.servlet.http.HttpServletResponse, handler: Any, @Nullable ex: Exception?) {
        MDC.remove("correlationId")
        correlationIdThreadLocal.remove()
    }
    
}
