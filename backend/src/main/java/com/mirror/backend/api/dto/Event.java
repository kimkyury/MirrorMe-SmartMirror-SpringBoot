package com.mirror.backend.api.dto;

import ch.qos.logback.core.status.Status;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.google.api.services.calendar.model.ConferenceSolution;
import com.google.api.services.calendar.model.ConferenceSolutionKey;
import com.google.api.services.calendar.model.EntryPoint;
import lombok.Builder;
import lombok.NoArgsConstructor;

import java.util.List;

public class Event {
    private @JsonProperty("kind") String kind;
    private @JsonProperty("etag") String etag;
    private @JsonProperty("summary") String summary;
    private @JsonProperty("updated") String updated;
    private @JsonProperty("timeZone") String timeZone;
    private @JsonProperty("accessRole") String accessRole;

    private @JsonProperty("defaultReminders") List<Reminder> defaultReminders;
    private @JsonProperty("nextSyncToken") String nextSyncToken;
    private @JsonProperty("items") List<Item> items;

    public Event() {}
    @Builder
    public Event(String kind, String etag, String summary, String updated, String timeZone, String accessRole, String nextSyncToken, List<Item> items) {
        this.kind = kind;
        this.etag = etag;
        this.summary = summary;
        this.updated = updated;
        this.timeZone = timeZone;
        this.accessRole = accessRole;
        this.nextSyncToken = nextSyncToken;
        this.items = items;
    }
    public static class Reminder {
        private @JsonProperty("method") String method;
        private @JsonProperty("minutes") int minutes;
    }
    public static class Item {
        private @JsonProperty("kind") String kind;
        private @JsonProperty("etag") String etag;
        private @JsonProperty("id") String id;
        private @JsonProperty("status") String status;
        private @JsonProperty("htmlLink") String htmlLink;
        private @JsonProperty("created") String created;
        private @JsonProperty("updated") String updated;
        private @JsonProperty("summary") String summary;
        private @JsonProperty("creator") Creator creator;
        private @JsonProperty("organizer") Organizer organizer;
        private @JsonProperty("start") StartEndDateTime start;
        private @JsonProperty("end") StartEndDateTime end;
        private @JsonProperty("iCalUID") String iCalUID;
        private @JsonProperty("sequence") int sequence;
        private @JsonProperty("attendees") List<Attendee> attendees;
        private @JsonProperty("hangoutLink") String hangoutLink;
        private @JsonProperty("eventType") String eventType;

        public Item() {}
        @Builder
        public Item(String kind, String etag, String id, String status, String htmlLink, String created, String updated, String summary, Creator creator, Organizer organizer, StartEndDateTime start, StartEndDateTime end, String iCalUID, int sequence, List<Attendee> attendees, String hangoutLink, String eventType) {
            this.kind = kind;
            this.etag = etag;
            this.id = id;
            this.status = status;
            this.htmlLink = htmlLink;
            this.created = created;
            this.updated = updated;
            this.summary = summary;
            this.creator = creator;
            this.organizer = organizer;
            this.start = start;
            this.end = end;
            this.iCalUID = iCalUID;
            this.sequence = sequence;
            this.attendees = attendees;
            this.hangoutLink = hangoutLink;
            this.eventType = eventType;
        }
    }

    @NoArgsConstructor
    public static class Organizer {
        private @JsonProperty("email") String email;
    }

    @NoArgsConstructor
    public static class StartEndDateTime {
        private @JsonProperty("dateTime") String dateTime;
        private @JsonProperty("timeZone") String timeZone;
    }

    @NoArgsConstructor
    public static class Attendee {
        private @JsonProperty("email") String email;
        private @JsonProperty("organizer") boolean organizer;
        private @JsonProperty("responseStatus") String responseStatus;
    }

    @NoArgsConstructor
    public static class ConferenceData {
        private @JsonProperty("createRequest") CreateRequest createRequest;
        private @JsonProperty("entryPoints") List<EntryPoint> entryPoints;
        private @JsonProperty("conferenceSolution") ConferenceSolution conferenceSolution;
        private @JsonProperty("conferenceId") String conferenceId;
    }

    @NoArgsConstructor
    public static class CreateRequest {
        private @JsonProperty("requestId") String requestId;
        private @JsonProperty("conferenceSolutionKey") ConferenceSolutionKey conferenceSolutionKey;
        private @JsonProperty("status") Status status;
    }

    @NoArgsConstructor
    public static class Creator {
        private @JsonProperty("email") String email;
    }

}

