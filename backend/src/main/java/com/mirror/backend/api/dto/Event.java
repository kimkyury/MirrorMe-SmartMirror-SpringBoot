package com.mirror.backend.api.dto;

import ch.qos.logback.core.status.Status;
import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.google.api.services.calendar.model.ConferenceSolution;
import com.google.api.services.calendar.model.ConferenceSolutionKey;
import com.google.api.services.calendar.model.EntryPoint;
import lombok.Getter;
import lombok.NoArgsConstructor;

import java.util.List;

@Getter
@NoArgsConstructor
@JsonIgnoreProperties(ignoreUnknown = true)
public class Event {
    @JsonProperty("kind")
    private String kind;
    @JsonProperty("etag")
    private String etag;
    @JsonProperty("summary")
    private String summary;
    @JsonProperty("updated")
    private String updated;
    @JsonProperty("timeZone")
    private String timeZone;
    @JsonProperty("accessRole")
    private String accessRole;
    @JsonProperty("defaultReminders")
    private List<Reminder> defaultReminders;
    @JsonProperty("nextSyncToken")
    private String nextSyncToken;
    @JsonProperty("items")
    private List<Item> items;

    @Override
    public String toString() {
        return "Event{" +
                "kind='" + kind + '\'' +
                ", etag='" + etag + '\'' +
                ", summary='" + summary + '\'' +
                ", updated='" + updated + '\'' +
                ", timeZone='" + timeZone + '\'' +
                ", accessRole='" + accessRole + '\'' +
                ", defaultReminders=" + defaultReminders +
                ", nextSyncToken='" + nextSyncToken + '\'' +
                ", items=" + items +
                '}';
    }

    @NoArgsConstructor
    @JsonIgnoreProperties(ignoreUnknown = true)
    public static class Reminder {
        @JsonProperty("method")
        private String method;
        @JsonProperty("minutes")
        private int minutes;
    }

    @Getter
    @NoArgsConstructor
    @JsonIgnoreProperties(ignoreUnknown = true)
    public static class Item {
        @JsonProperty("kind")
        private String kind;
        @JsonProperty("etag")
        private String etag;
        @JsonProperty("id")
        private String id;
        @JsonProperty("status")
        private String status;
        @JsonProperty("htmlLink")
        private String htmlLink;
        @JsonProperty("created")
        private String created;
        @JsonProperty("updated")
        private String updated;
        @JsonProperty("summary")
        private String summary;
        @JsonProperty("creator")
        private Creator creator;
        @JsonProperty("organizer")
        private Organizer organizer;
        @JsonProperty("start")
        private StartEndDateTime start;
        @JsonProperty("end")
        private StartEndDateTime end;
        @JsonProperty("iCalUID")
        private String iCalUID;
        @JsonProperty("sequence")
        private int sequence;
        @JsonProperty("attendees")
        private List<Attendee> attendees;
        @JsonProperty("hangoutLink")
        private String hangoutLink;
        @JsonProperty("eventType")
        private String eventType;
    }

    @Getter
    @NoArgsConstructor
    @JsonIgnoreProperties(ignoreUnknown = true)
    public static class Organizer {
        @JsonProperty("email")
        private String email;
    }

    @Getter
    @NoArgsConstructor
    @JsonIgnoreProperties(ignoreUnknown = true)
    public static class StartEndDateTime {
        @JsonProperty("dateTime")
        private String dateTime;
        @JsonProperty("timeZone")
        private String timeZone;
    }
    @Getter
    @NoArgsConstructor
    @JsonIgnoreProperties(ignoreUnknown = true)
    public static class Attendee {
        @JsonProperty("email")
        private String email;
        @JsonProperty("organizer")
        private boolean organizer;
        @JsonProperty("self")
        private boolean self;
        @JsonProperty("responseStatus")
        private String responseStatus;
    }
    @Getter
    @NoArgsConstructor
    @JsonIgnoreProperties(ignoreUnknown = true)
    public static class ConferenceData {
        @JsonProperty("createRequest")
        private CreateRequest createRequest;
        @JsonProperty("entryPoints")
        private List<EntryPoint> entryPoints;
        @JsonProperty("conferenceSolution")
        private ConferenceSolution conferenceSolution;
        @JsonProperty("conferenceId")
        private String conferenceId;
    }
    @Getter
    @NoArgsConstructor
    @JsonIgnoreProperties(ignoreUnknown = true)
    public static class CreateRequest {
        @JsonProperty("requestId")
        private String requestId;
        @JsonProperty("conferenceSolutionKey")
        private ConferenceSolutionKey conferenceSolutionKey;
        @JsonProperty("status")
        private Status status;
    }
    @Getter
    @NoArgsConstructor
    @JsonIgnoreProperties(ignoreUnknown = true)
    public static class Creator {
        @JsonProperty("email")
        private String email;
    }

}

