Incident Postmortem Report
By
Carl Munene
Senior Engineer
Safaricom - Masoko Product Line

Issue Summary:

Duration:
Start Time: April 15, 2024, 02:30 EST
End Time: April 15, 2024, 06:45 EST

Impact:
The outage affected our entire cloud infrastructure hosted at the Thika data center, resulting in a complete loss of services for approximately 60% of our users during the downtime. Users experienced unavailability of applications and data, leading to disruptions in business operations.

Root Cause:
The root cause was identified as a power outage at the Thika data center, compounded by the failure of one of the backup generators, which was not automatically brought online as intended.

Timeline:

Detection Time:
April 15, 2024, 02:35 EST

Detection Method:
Monitoring systems triggered alerts for the sudden loss of connectivity to servers hosted at the Thika data center.

Actions Taken:
Investigated network connectivity issues and initially assumed a potential network hardware failure.
Checked with the data center staff for any ongoing maintenance or known issues.
Onsite personnel reported a power outage at the data center.

Misleading Paths:
Focused initially on network-related issues, overlooking the possibility of a broader data center problem.
Assumed a potential network hardware failure without considering external factors like power outages.

Escalation:
Escalated to the Data Center Operations team for detailed information and collaboration.

Resolution:
Identified the power outage as the primary cause.
Discovered that one of the backup generators failed to start automatically.

Collaborated with data center staff to restore power, bringing affected servers back online.

Root Cause and Resolution:

Root Cause:
The root cause was a power outage at the Thika data center, exacerbated by the failure of one backup generator, which did not start automatically as intended.

Resolution:
To address the issue, we collaborated with data center staff to restore power and manually started the backup generator. Additionally, we implemented procedures to enhance the automatic failover mechanisms of backup generators in the event of power disruptions.

Corrective and Preventative Measures:

Improvements/Fixes:
Generator Failover Testing: Regularly test and simulate scenarios to ensure all backup generators start automatically in case of power outages.
Enhanced Monitoring: Implement additional monitoring for power status at the data center level to detect and respond to outages more efficiently.
Communication Protocols: Establish clear communication protocols with the data center staff to receive prompt and accurate updates during incidents.

Tasks:
Emergency Response Drills: Conduct emergency response drills with the team to simulate power-related outages and practice swift and coordinated responses.
Documentation Update: Update documentation to include specific procedures for handling data center-wide outages and generator failures.
Audit and Compliance: Regularly audit and review compliance with data center protocols and standards to ensure alignment with best practices.

By implementing these corrective and preventative measures, we aim to fortify the resilience of our infrastructure against external factors like power outages and ensure a more robust and reliable service for our users.
