import React, { useState, useEffect } from "react";
import axios from "axios";
import { Calendar, momentLocalizer } from "react-big-calendar";
import moment from "moment";
import NavBar from "./NavBar";
import "react-big-calendar/lib/css/react-big-calendar.css";

const localizer = momentLocalizer(moment);

function CalendarPage() {
  const [events, setEvents] = useState([]);

  useEffect(() => {
    console.log("test");
    axios
      .get("/api/events/")
      .then((response) => {
        console.log("chips : ", response.data[0]);
        const events = response.data.map((event) => ({
          start: new Date(event.day),
          end: new Date(event.end_day),
        }));
        setEvents(events);
        console.log("EVENTS ::: ", events);
      })
      .catch((error) => console.log(error));
  }, []);

  console.log("EVENT 2 :: ", events);
  return (
    <div>
      <NavBar />
      <h2>Mon Calendrier</h2>
      <Calendar
        localizer={localizer}
        events={events}
        startAccessor="start"
        endAccessor="end"
        style={{ height: 500 }}
      />
    </div>
  );
}
export default CalendarPage;
