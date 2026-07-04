import heapq

class solution:
    def addPatient(self, patients, severity, name):
        # Push (-severity, name) so highest severity comes first
        heapq.heappush(patients, (-severity, name))

    def treatPatient(self, patients):
        # Remove and print the highest severity patient
        if patients:
            severity, name = heapq.heappop(patients)
            print(name)

    def displayNextPatient(self, patients):
        # Display the next patient without removing
        if patients:
            print(patients[0][1])