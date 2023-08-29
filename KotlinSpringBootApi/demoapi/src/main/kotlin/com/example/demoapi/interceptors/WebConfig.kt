package com.example.demoapi.config

import com.example.demoapi.interceptors.CorrelationInterceptor
import org.springframework.stereotype.Component
import org.springframework.web.servlet.config.annotation.InterceptorRegistry
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer

@Component
class WebConfig(private val correlationInterceptor: CorrelationInterceptor) : WebMvcConfigurer {
    
    override fun addInterceptors(registry: InterceptorRegistry) {
        registry.addInterceptor(correlationInterceptor)
    }
}
