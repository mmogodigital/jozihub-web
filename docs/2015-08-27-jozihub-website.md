# JoziHub website updates
## Objective
Praeklet Foundation has been tasked with updating JoziHub's website.

This document outlines the scope of the work, the time in which it should be completed, its cost and the assumptions that were made.

## Scope of Work
### Register GitHub organization and move jozihub-web code base
JoziHub's code for the website is currently here: [https://github.com/praekelt/jozihub-web](https://github.com/praekelt/jozihub-web). This is to be moved to it's own GitHub organization.

Github issue | Estimated effort
------------ | ----------------
n/a          | 1 hour

Praekelt will:
- Move the jozihub repository from Praekelt's organization to JoziHub's.

JoziHub will:
- Provide the Github organization

### E-mail registration and confirmation
> Upon registration a customer should receive a welcome response to the person registered.

Github issue                                                                                           | Estimated effort
------------------------------------------------------------------------------------------------------ | ----------------
[https://github.com/praekelt/jozihub-web/issues/16](https://github.com/praekelt/jozihub-web/issues/16) | 1 hour

Investigation into the current code-base shows that e-mails should be sent out.

Praekelt Foundation will:
- troubleshoot and diagnose why this is not happening
- update the content of the mail with supplied copy from JoziHub
- Add BCC capability to the emailer to notify JoziHub

### Database accessed
> We would like to be able to download the full database with just the basic information (name, surname, affiliation, e-mail address, mobile number only) onto an excel doc from the website or have it feed directly into a google doc so it can be easily accessed.

Github issue                                                                                         | Estimated effort
---------------------------------------------------------------------------------------------------- | ----------------
[https://github.com/praekelt/jozihub-web/issues/6](https://github.com/praekelt/jozihub-web/issues/6) | 8 hours

Praekelt will:
- Enable an excel export of this data

### Menu changes - News to change to blog
> This should link to the tumblr blog. We will start to use the Tumblr blog for stories about JoziHub / press releases. Facebook and twitter will still remain the main source for up to date news.

Github issue                                     | Estimated effort
------------------------------------------------ | ----------------
https://github.com/praekelt/jozihub-web/issues/7 | 0.5 hours

Praekelt will:
- Change the News link on the website to the blog as directed

JoziHub will:
- Supply the link to the blog

### Carousel
> Second image on site: The image with pictures of people and icons. Can we change this to be of some of our actual startups and their logos? when you click on this image it should take you to the page with the startup listings.

Github issue                                                  | Estimated effort
------------------------------------------------------------- | ----------------
https://github.com/praekelt/jozihub-web/issues/12  (Point 1.) | 4 hours

Praekelt will:
- Implement a carousel on the front page, based on startup company images

### New Events layout
> This should still list our events but we feel there could be a better way of showcasing the events each month - perhaps each event in a cube with an image and logo that you can click through to the full details? We need to add a line that says "if you'd like your event listed on the JoziHub website please send the details through to rea@jozihub.org"

Github issue                                     | Estimated effort
------------------------------------------------ | ----------------
https://github.com/praekelt/jozihub-web/issues/8 | 2 hours

Praeklet will:
- Implement the new design for the events supplied by JoziHub

JoziHub will:
- Supply a new HTML design for implementation

### Membership options
> There are five membership options:
  1. **Community Member**: Anyone interested or involved in technology, entrepreneurship, business, government, social impact and more can join the JoziHub Community to receive our newsletter, find out about events and happenings and get involved
  2. **Resident Startup Member**: Tech Startup companies can apply for permanent or semi-permanent workspace at JoziHub as a resident startup member
  3. **Social Impact Member**: Social Impact organisations or NGO's can apply for permanent or semi-permanent workspace at JoziHub as a social impact member
  4. **Developer Network Member**: Individual developers can apply for ad hoc use of the JoziHub co-working space for free
  5. **Mentorship Member**: Individuals or companies who would like to give of their time, experience and expertise to mentor the JoziHub Resident Startups

> There should be a clickable button within this section at the top that says 'click here to register' that takes you to the application page

Prakelet will:
- implement refined HTML design
- we will investigate data storage of registrations

JoziHub will:
- membership page
- Supply simplified HTML design

Github issue                                     | Estimated effort
------------------------------------------------ | ----------------
https://github.com/praekelt/jozihub-web/issues/9 | 3 hours

Praekelt will:
- Investigate what is required for this issue

### Partners layout

Github issue                                      | Estimated effort
------------------------------------------------- | ----------------
https://github.com/praekelt/jozihub-web/issues/11 | 2 hours

> List of partners, this should again be more user friendly, perhaps blocks again with the logos that you can scroll over to see more info.

Praekelt will:
- Implement the design supplied by JoziHub

JoziHub will:
- Supply new design for partners page.

### Startup Companies
> Gallery  Companies - this is a list of our startups. We should be able to upload a logo, upload a pic of them and insert a short profile with contact details. There are some really wonderful examples to be found below as suggested by Andy at Google: [http://www.flat6labs.com/companies/](http://www.flat6labs.com/companies/) (this is our favourite) [http://www.thegreekcampus.com/#!greek-building/c1wj7](http://www.thegreekcampus.com/#!greek-building/c1wj7) [http://www.galatabusinessangels.com/en/portfolio](http://www.galatabusinessangels.com/en/portfolio)

> Information to capture per startup (currently 30 startups but this will increase):

```
Name
Logo
20 word short descriptor
150 word long descriptor
Founder photographs
Link to their website
Social media profiles
Contact details
```

Github issue                                      | Estimated effort
------------------------------------------------- | ----------------
https://github.com/praekelt/jozihub-web/issues/14 | 4 hours

Praekelt will:
- Remove the gallery link from the site
- Implement a new model for startups
- Provide training on how to use the new startup model
- Implement the design as supplied by JoziHub

JoziHub will:
- Supply the HTML design for the new Companies model

### Other
> First image at the top of the site - is it possible to change this at all to reflect an image of the hub. This will be provided.  

> Inclusion of our JoziHub metrics on the front page of the site: See this link for example of how this could work: [http://www.flat6labs.com/](http://www.flat6labs.com/)

> JoziHub metrics would be:

```
Resident Startup Companies
Jobs Created
Events
Community members
```

Github issue                                      | Estimated effort
------------------------------------------------- | ----------------
https://github.com/praekelt/jozihub-web/issues/12 | 16 hours

Praekelt will:
- Replace JoziHub image
- Expose the metrics
- Assist with the design supplied by JoziHub

JoziHub will:
- Supply HTML design for the metrics and inclusion on the home page

## Update galleries

Github issue                                      | Estimated effort
------------------------------------------------- | ----------------
https://github.com/praekelt/jozihub-web/issues/17 | 3 hours

Praekelt will:
- Investigate pulling instagram pictures onto the gallery
- Write an instagram integration to pull photos from there

JoziHub will:
- Supply HTML layout for the gallery

## Remove Jobs
Praekelt will:
- remove "Jobs"
- remove "Sign in"

menu items.

## Book a venue
Praekelt will:
- Supply a form to email
- Validate form to email subscription

Github issue                                      | Estimated effort
------------------------------------------------- | ----------------
https://github.com/praekelt/jozihub-web/issues/18 | 3 hours

## Update footer
Praekelt will:
- Implement new footer

JoziHub will:
- Supply new footer

Github issue                                      | Estimated effort
------------------------------------------------- | ----------------
https://github.com/praekelt/jozihub-web/issues/19 | 0.5 hour

## Excluded from scope
- Multiple application forms, we will only be simplifying the current application form
- Integrate Inspiration Labs off.

## Cost
The cost of these updates are calculated as the total number of estimated hours.

Once the scope of work has been approved a cost estimate will be supplied to JoziHub.

On approval a 50% deposit is required.

## Assumptions
- Work will commence 10 working days after the cost estimate has been approved.
- Praekelt will be minimally involved with the design of the site.
- Each issue will be tracked in GitHub under their respective issues and will lead towards a milestone.
- Deadlines and delivery dates can only be confirmed once deposit is made and estimated efforts are not a guarantee of scheduled delivery.
