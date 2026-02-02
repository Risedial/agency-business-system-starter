# Phase 3: Prompt Generator Tool

## Prerequisites
- Phase 1-2 complete (all docs and framework files created)
- STATE.json exists in `/system`
- Business configured in CLAUDE.md (Niche, Offer, Price)

## Deliverables
- `/system/prompt-generator.html` - Single-file React application

## Instructions

### Build the Prompt Generator

Create `/system/prompt-generator.html` as a self-contained HTML file with embedded React and Tailwind CSS via CDN.

**Core Functionality:**

1. **Automatic State Loading:**
   - Load `../system/STATE.json` on page load
   - Display "Refresh State" button to reload
   - Fall back gracefully if STATE.json doesn't exist
   - Show loaded state in read-only summary section

2. **State Display:**
   - Current Phase
   - Niche, Offer Promise, Price Point
   - Metrics: Connections Built, Videos Sent, Clients Acquired, Offer Validated
   - Last Updated timestamp

3. **"What's Next?" Recommendation:**
   - Implement decision logic based on loaded state
   - Display next recommended action prominently

4. **Dynamic Prompt Generation:**
   - 7 categories: Validation, Offer Development, Sales Assets, Lead Generation, Fulfillment, Scaling, Custom
   - Each category has multiple prompt templates
   - Generated prompts include current state context
   - Copy to clipboard functionality

**Implementation Approach:**

Due to the complexity of building this in one shot, we'll create it in 3 sub-phases:

---

### Phase 3A: Basic Structure & State Loading

Create initial HTML file with:
- HTML structure
- React and Tailwind CDN links
- State loading function
- Basic display of loaded state

**Code structure:**
```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Agency Business System - Prompt Generator</title>
    <script crossorigin src="https://unpkg.com/react@18/umd/react.production.min.js"></script>
    <script crossorigin src="https://unpkg.com/react-dom@18/umd/react-dom.production.min.js"></script>
    <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-50">
    <div id="root"></div>
    <script type="text/babel">
        // State loading logic
        async function loadState() {
            try {
                const response = await fetch('./STATE.json');
                if (!response.ok) throw new Error('STATE.json not found');
                const state = await response.json();
                return state;
            } catch (e) {
                console.log('Using default state');
                return {
                    currentPhase: 'Phase 1',
                    niche: '',
                    offerPromise: '',
                    pricePoint: '',
                    metrics: {
                        connectionsBuilt: 0,
                        postsPublished: 0,
                        videosSent: 0,
                        clientsAcquired: 0,
                        offerValidated: false
                    },
                    lastUpdated: null
                };
            }
        }

        // React component
        function PromptGenerator() {
            const [state, setState] = React.useState(null);
            const [loading, setLoading] = React.useState(true);

            React.useEffect(() => {
                loadState().then(data => {
                    setState(data);
                    setLoading(false);
                });
            }, []);

            const refreshState = async () => {
                setLoading(true);
                const data = await loadState();
                setState(data);
                setLoading(false);
            };

            if (loading) return <div className="p-8">Loading...</div>;

            return (
                <div className="container mx-auto p-6 max-w-4xl">
                    <h1 className="text-3xl font-bold mb-6">Agency Business System</h1>

                    <div className="bg-white rounded-lg shadow p-6 mb-6">
                        <div className="flex justify-between items-center mb-4">
                            <h2 className="text-xl font-semibold">Current State</h2>
                            <button
                                onClick={refreshState}
                                className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600"
                            >
                                Refresh State
                            </button>
                        </div>

                        <div className="grid grid-cols-2 gap-4">
                            <div>
                                <p className="text-sm text-gray-600">Phase</p>
                                <p className="font-medium">{state.currentPhase}</p>
                            </div>
                            <div>
                                <p className="text-sm text-gray-600">Niche</p>
                                <p className="font-medium">{state.niche || 'Not set'}</p>
                            </div>
                            <div>
                                <p className="text-sm text-gray-600">Offer Promise</p>
                                <p className="font-medium">{state.offerPromise || 'Not set'}</p>
                            </div>
                            <div>
                                <p className="text-sm text-gray-600">Price Point</p>
                                <p className="font-medium">{state.pricePoint || 'Not set'}</p>
                            </div>
                            <div>
                                <p className="text-sm text-gray-600">Connections</p>
                                <p className="font-medium">{state.metrics.connectionsBuilt}/100</p>
                            </div>
                            <div>
                                <p className="text-sm text-gray-600">Videos Sent</p>
                                <p className="font-medium">{state.metrics.videosSent}</p>
                            </div>
                            <div>
                                <p className="text-sm text-gray-600">Clients</p>
                                <p className="font-medium">{state.metrics.clientsAcquired}</p>
                            </div>
                            <div>
                                <p className="text-sm text-gray-600">Offer Validated</p>
                                <p className="font-medium">{state.metrics.offerValidated ? 'Yes' : 'No'}</p>
                            </div>
                        </div>
                    </div>

                    {/* Prompt generation UI will go here in Phase 3B */}
                </div>
            );
        }

        ReactDOM.render(<PromptGenerator />, document.getElementById('root'));
    </script>
</body>
</html>
```

**Test:** Open in browser, verify state loads and displays correctly.

---

### Phase 3B: Add "What's Next?" Logic & Prompt Categories

Add to the React component:

**"What's Next?" function:**
```javascript
function getNextAction(state) {
    const { metrics, niche, offerPromise, currentPhase } = state;

    // Phase checks
    if (currentPhase === "Not Started" || currentPhase === "Phase 1" || currentPhase === "Phase 2") {
        return "Complete system initialization first. Run /init command.";
    }

    if (currentPhase === "Phase 3") {
        return "You're building this tool right now! Complete Phase 3 to continue.";
    }

    if (currentPhase === "Phase 4") {
        return "Create asset templates. Execute .claude/rules/phase-4-assets.md";
    }

    if (currentPhase === "Phase 5") {
        return "Set up daily operations. Execute .claude/rules/phase-5-operations.md";
    }

    if (currentPhase === "Phase 6") {
        return "Run final validation. Execute .claude/rules/phase-6-validation.md";
    }

    // Business configuration check
    if (!niche || !offerPromise) {
        return "Configure your business in CLAUDE.md (Niche, Offer Promise, Price Point)";
    }

    // Daily operations logic
    if (metrics.connectionsBuilt < 100) {
        return "Build your network: Add 20-30 targeted connections daily until you reach 100";
    }

    if (!metrics.offerValidated && metrics.postsPublished < 3) {
        return "Post hand raiser content to validate your offer (need 3+ engaged prospects)";
    }

    if (!metrics.offerValidated && metrics.postsPublished >= 3) {
        return "Review engagement - if minimal, pivot your offer promise and test again";
    }

    if (metrics.offerValidated && metrics.videosSent === 0) {
        return "Record your first sales video and send to engaged prospects";
    }

    if (metrics.videosSent > 0 && metrics.clientsAcquired === 0) {
        return "Execute follow-up sequence on all video recipients";
    }

    if (metrics.clientsAcquired < 3) {
        return "Focus on acquisition: Post hand raisers daily and send videos to all responders";
    }

    if (metrics.clientsAcquired >= 10) {
        return "Hiring is MANDATORY - generate job post via Scaling category below";
    }

    if (metrics.clientsAcquired >= 5) {
        return "Consider hiring - use Scaling category to generate job post";
    }

    return "Continue daily operations (see /daily/QUICK-REFERENCE.md for checklist)";
}
```

**Display "What's Next?" prominently:**
```jsx
<div className="bg-blue-50 border-l-4 border-blue-500 p-6 mb-6">
    <h3 className="text-lg font-semibold mb-2">📋 What Should I Do Next?</h3>
    <p className="text-gray-700">{getNextAction(state)}</p>
</div>
```

**Add prompt category dropdown:**
```jsx
const [selectedCategory, setSelectedCategory] = React.useState('validation');
const [selectedPrompt, setSelectedPrompt] = React.useState('');

const categories = {
    validation: [
        { id: 'validate-offer', name: 'Generate hand raiser post for testing offer' },
        { id: 'analyze-engagement', name: 'Analyze post engagement and recommend pivot or proceed' },
        { id: 'alternative-angles', name: 'Generate alternative offer angles' }
    ],
    sales: [
        { id: 'video-script', name: 'Write 5-minute video script' },
        { id: 'message-wrappers', name: 'Generate video message wrapper templates' },
        { id: 'follow-up', name: 'Create follow-up sequence' },
        { id: 'objections', name: 'Generate objection handling scripts' }
    ],
    leadgen: [
        { id: 'hand-raiser-posts', name: 'Generate 10 hand raiser post variations' },
        { id: 'response-templates', name: 'Create response templates for hand raisers' }
    ],
    fulfillment: [
        { id: 'onboarding-doc', name: 'Create client onboarding document' },
        { id: 'weekly-update', name: 'Generate weekly update Loom script template' }
    ],
    scaling: [
        { id: 'job-post', name: 'Generate job post for hiring' },
        { id: 'test-assignment', name: 'Create test assignment for candidates' }
    ]
};

<select
    value={selectedCategory}
    onChange={(e) => setSelectedCategory(e.target.value)}
    className="w-full p-2 border rounded"
>
    <option value="validation">Validation Phase</option>
    <option value="sales">Sales Assets</option>
    <option value="leadgen">Lead Generation</option>
    <option value="fulfillment">Fulfillment</option>
    <option value="scaling">Scaling</option>
</select>
```

**Test:** Category selection works, "What's Next?" displays correctly.

---

### Phase 3C: Add Prompt Generation & Copy Functionality

Add prompt template generation:

```javascript
function generatePrompt(promptId, state) {
    const baseContext = `
## Context
You are working in an Agency Business System workspace.

**Current State:**
- Phase: ${state.currentPhase}
- Niche: ${state.niche || 'Not set'}
- Offer Promise: ${state.offerPromise || 'Not set'}
- Price Point: ${state.pricePoint || 'Not set'}
- Connections Built: ${state.metrics.connectionsBuilt}/100
- Videos Sent: ${state.metrics.videosSent}
- Clients Acquired: ${state.metrics.clientsAcquired}
- Offer Validated: ${state.metrics.offerValidated ? 'Yes' : 'No'}

## Reference Files
- /CLAUDE.md (workspace context)
- /.claude/rules/reference/*.md (methodology details)
- /docs/*.md (framework documents)

---
`;

    const prompts = {
        'validate-offer': baseContext + `
## Task
Generate a hand raiser social media post to test the current offer promise.

**Requirements:**
1. Use the niche and offer promise from current state
2. Format as a direct question asking "who needs [specific outcome]?"
3. Focus on the PROMISE (what they get), not the mechanism (what you do)
4. Make it specific and measurable
5. Include budget anchor if appropriate

**Output Format:**
Provide 3 variations of the post, optimized for the platform (LinkedIn or Facebook based on niche).

**Save to:** User will copy and post manually

**After posting:**
- Update CLAUDE.md → Posts Published: [increment]
- Track engagement (comments + DMs)
- 3+ engaged prospects = offer validated`,

        'video-script': baseContext + `
## Task
Write a complete 5-minute async video sales script using the 5-part structure.

**Requirements:**
1. Hook (10-15 sec): Reference prospect's specific situation
2. Outcome Demo (60-90 sec): Show what happens after they work with you
3. Contextualized Price (20-30 sec): Always pair price with deliverable
4. Differentiation (30-45 sec): Address "tried before" objection
5. Purchase Instructions (20-30 sec): Exact steps to buy

**Include:**
- Screen recording instructions for outcome demonstration
- Specific language for price presentation
- One key differentiator (speed, process, or guarantee)
- Exact payment flow steps

**Output Format:**
Complete script with timing markers and visual cues

**Save to:** /assets/video-script-CUSTOM.md

**After completion:**
- Update CLAUDE.md → Assets Created: [add file]`,

        'hand-raiser-posts': baseContext + `
## Task
Generate 10 hand raiser post template variations for the current niche and offer.

**Requirements:**
1. All variations focus on same offer promise but different angles
2. Include fill-in-the-blank sections: [like this]
3. Mix of formats: direct question, time-bound, budget anchor, pain focus, case study hook
4. Optimize for platform (LinkedIn professional tone OR Facebook casual tone)
5. Each under 150 words

**Output Format:**
Markdown file with 10 numbered templates, each with:
- Template text
- Platform recommendation (LinkedIn/Facebook)
- Best posting time

**Save to:** /assets/hand-raiser-posts-GENERATED.md

**After creation:**
- Update CLAUDE.md → Assets Created: [add file]
- Use templates for daily posting`,

        'onboarding-doc': baseContext + `
## Task
Create a client onboarding document template for the current service offering.

**Requirements:**
1. Welcome message with expectation setting
2. "No-meeting" model explanation (positioned as benefit)
3. Communication protocol (Loom updates, response times)
4. Required information/access checklist
5. Timeline for first deliverable
6. How to contact for issues

**Include:**
- Specific timeline based on service type
- Explicit statement: "We don't do status calls - here's why this benefits you"
- Response time commitment (e.g., "4 hours during business hours")

**Output Format:**
Email template (subject + body) ready to copy and send

**Save to:** /assets/onboarding-template-CUSTOM.md

**After creation:**
- Update CLAUDE.md → Assets Created: [add file]
- Use for all new client onboardings`,

        'job-post': baseContext + `
## Task
Generate a job post for hiring the first team member.

**Determine role priority:**
- If clientsAcquired >= 10: Fulfillment Specialist (URGENT)
- If clientsAcquired >= 5: Fulfillment Specialist OR Account Manager
- If clientsAcquired < 5: Wait, focus on acquisition

**Requirements:**
1. Job title and remote contract position statement
2. What they'll do (3-5 specific tasks based on service type)
3. Requirements (skills, availability, self-directed nature)
4. Compensation range
5. How to apply (test assignment, not resume)

**Include:**
- Test assignment description that evaluates skill without revealing full business model
- Evaluation rubric

**Output Format:**
Complete job post ready to publish + test assignment

**Save to:** /assets/job-post-GENERATED.md

**After creation:**
- Update CLAUDE.md → Assets Created: [add file]
- Post to relevant job boards`
    };

    return prompts[promptId] || 'Prompt template not found';
}
```

**Add copy to clipboard:**
```jsx
const [generatedPrompt, setGeneratedPrompt] = React.useState('');
const [copied, setCopied] = React.useState(false);

const handleGenerate = (promptId) => {
    const prompt = generatePrompt(promptId, state);
    setGeneratedPrompt(prompt);
};

const copyToClipboard = () => {
    navigator.clipboard.writeText(generatedPrompt);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
};

<div>
    <textarea
        value={generatedPrompt}
        readOnly
        rows={20}
        className="w-full p-4 border rounded font-mono text-sm"
    />
    <button
        onClick={copyToClipboard}
        className="mt-2 bg-green-500 text-white px-6 py-2 rounded hover:bg-green-600"
    >
        {copied ? '✓ Copied!' : 'Copy to Clipboard'}
    </button>
</div>
```

**Test:** Generate prompts, verify they include current state, copy to clipboard works.

---

## Quality Criteria

Before marking complete:
- [ ] prompt-generator.html file created (1,000+ lines)
- [ ] Opens in browser without errors
- [ ] STATE.json loads automatically on page load
- [ ] "Refresh State" button reloads state successfully
- [ ] Current state displays all fields (phase, niche, metrics)
- [ ] "What's Next?" recommendation displays correctly
- [ ] Can select from all 7 categories
- [ ] Can generate prompts from each category
- [ ] Generated prompts include current workspace state
- [ ] Copy to clipboard works with visual confirmation
- [ ] Mobile-responsive layout (test on narrow browser window)

## Validation

Open prompt-generator.html in browser and verify:
1. No console errors (F12 → Console tab)
2. State section shows current metrics
3. "What's Next?" provides relevant recommendation
4. Category dropdown has all options
5. Generate button produces prompt with current state context
6. Copy button works and shows "Copied!" confirmation

## Next Phase

After completion:
- Update CLAUDE.md Phase to "Phase 4"
- User can now use prompt generator for all future prompt needs
- Proceed to Phase 4: Create Initial Assets
