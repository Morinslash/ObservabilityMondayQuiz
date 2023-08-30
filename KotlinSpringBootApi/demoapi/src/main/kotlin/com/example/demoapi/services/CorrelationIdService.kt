package com.example.demoapi.services

import org.slf4j.MDC
import org.springframework.stereotype.Service

@Service
class CorrelationIdService {

    private val correlationIdThreadLocal = ThreadLocal<String?>()

    fun getCorrelationId(): String? = correlationIdThreadLocal.get()

    fun setCorrelationId(correlationId: String) {
        correlationIdThreadLocal.set(correlationId)
        MDC.put("correlationId", correlationId)  // Set MDC here
    }

    fun clearCorrelationId() {
        correlationIdThreadLocal.remove()
        MDC.remove("correlationId")  // Clear MDC here
    }
}
