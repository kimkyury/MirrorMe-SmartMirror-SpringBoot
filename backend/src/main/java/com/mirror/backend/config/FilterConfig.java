package com.mirror.backend.config;

import com.mirror.backend.api.filter.TokenAuthenticationFilter;
import org.springframework.boot.web.servlet.FilterRegistrationBean;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class FilterConfig {

    @Bean
    public FilterRegistrationBean<TokenAuthenticationFilter> customFilter(){
        FilterRegistrationBean<TokenAuthenticationFilter> registrationBean = new FilterRegistrationBean<>();

        registrationBean.setFilter(new TokenAuthenticationFilter());
        registrationBean.addUrlPatterns("/schedule/**"); // 필터를 적용할 URL 패턴
        registrationBean.addUrlPatterns("/tasks/**");
        registrationBean.addUrlPatterns("/user/**");
//        registrationBean.addUrlPatterns("/search/*");
        registrationBean.addUrlPatterns("/signup/**");
        return registrationBean;
    }
}