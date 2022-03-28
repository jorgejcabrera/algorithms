requesters = {1: [1, 2, 3, 4], 2: [1, 3, 4, 2], 3: [2, 4, 3, 1], 4: [4, 2, 1, 3]}

requested = {1: [2, 3, 4, 1], 2: [4, 3, 1, 2], 3: [1, 2, 3, 4], 4: [3, 4, 2, 1]}


def requesters_alone(matches, requesters):
    print(requesters)
    return requesters.keys() - matches.keys()


def best_of(entities_with_preferences, requester_id):
    preferences = entities_with_preferences[requester_id]
    return preferences[0]


def main():
    print(requesters)

def already_matched(matches, best_requested):
    # TODO
    return False

if __name__ == "__main__":
    matches = {}
    requesters_alone = requesters_alone(matches, requesters)
    while len(requesters_alone) > 0:
        requester = requesters_alone.pop()
        best_requested = best_of(requesters, requester)

        # TODO
        if not already_matched(matches, best_requested):
            matches[requester] = best_requested
        else:
            best_requester = best_of(requested, best_requested)



print(requesters_alone)
